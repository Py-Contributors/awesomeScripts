# this is a code that get the price of bitcoin in USD
# through argument given from the user
import sys
import requests
import json

def main():

    msg = """
        Missing command-line argument
        Please Usage following :
        python bitcoin_price.py {0-99} {USD, EUR, or GPB}

        example :
        python bitcoin_price.py 1 usd
        """
    
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        o = response.json()
        bcoin = o['bpi'][sys.argv[2].upper()]['rate'].split(',')
        new_price = bcoin_converter(bcoin,float(sys.argv[1]))
        print(f'${int(new_price[0])},{new_price[1]:.4f}')
    except:
        sys.exit(msg)


def bcoin_converter(bcoin,n):
    new_price =[]
    new_price.append(float(bcoin[0]) * n)
    new_price[0] += float(bcoin[1]) * n // 1000
    new_price.append((float(bcoin[1]) * n % 1000))
    frag = str(new_price[0]).split('.')
    new_price[1] += float(frag[1]) * 100
    return new_price

if __name__ == "__main__":
    main()