# this is a code that get the price of bitcoin in USD
# through argument given from the user
import sys
import requests
import json



def main():
    if len(sys.argv) < 2 :
        sys.exit('Missing command-line argument')
    else:
        if sys.argv[1].isalpha() :
            sys.exit('Command-line argument is not a string')
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    o = response.json()
    bcoin = o['bpi'][sys.argv[2].upper()]['rate'].split(',')
    new_price = bcoin_converter(bcoin,float(sys.argv[1]))
    print(f'${int(new_price[0])},{new_price[1]:.4f}')


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