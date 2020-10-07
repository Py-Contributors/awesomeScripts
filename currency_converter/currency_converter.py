import json
import requests
from argparse import ArgumentParser


class CurrencyConverter:
    def __init__(self, fromCurrency, toCurrency, amount):
        self.fromCurrency = fromCurrency.upper()
        self.toCurrency = toCurrency.upper()
        self.amount = amount

    def convert(self):
        try:
            exchange_rate = self.get_exchange_rate()
            converted_amount = float(self.amount) * exchange_rate
            print("%s %s = %.2f %s (exchange rate: %s)" % (
                self.amount,
                self.fromCurrency,
                converted_amount,
                self.toCurrency,
                exchange_rate
            ))
        except Exception as err:
            print(err)

    def get_exchange_rate(self):
        api_url = 'https://api.exchangerate-api.com/v4/latest/'\
            + self.fromCurrency
        response = requests.get(api_url)
        json_response = json.loads(response.content.decode('utf-8'))

        if response.status_code == 200:
            if self.toCurrency not in json_response['rates']:
                raise Exception('To Currency not supported')

            return json_response['rates'][self.toCurrency]

        if(
            response.status_code == 404
            and json_response['error_type'] == 'unsupported_code'
        ):
            raise Exception('From Currency not supported')

        raise Exception('Could not get exchange rate')


parser = ArgumentParser()
parser.add_argument("-from", dest="From", default="usd",
                    help="From currency (eg: usd)", metavar="CURRENCY")
parser.add_argument("-to", dest="To", default="cad",
                    help="To currency (eg: usd)", metavar="CURRENCY")
parser.add_argument("-amount", dest="Amount", default=100,
                    help="Amount", metavar="AMOUNT")
args = parser.parse_args()

currency_converter = CurrencyConverter(args.From, args.To, args.Amount)
currency_converter.convert()
