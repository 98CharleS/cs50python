import requests
import sys

try:
    data = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    rate = data.json()['bpi']['USD']['rate_float']
    amount = rate * float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")
except IndexError:
    sys.exit("Missing command-line argument")
else:
    print(f"${amount:,.4f}")
