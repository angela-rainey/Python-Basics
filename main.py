#request price of bitcoin 
# (5 different types of coin display spot price, name, and exchange rates)
#get a notification whenever the price changes
#ability to save the data to a csv file

import requests 
import json
def get_currency(currency_abbrev):
    r = requests.get('https://api.coinbase.com/v2/exchange-rates?currency=' + currency_abbrev)
    rjson = r.json()
    return rjson

btc_exch_rate = get_currency('BTC')
xrp_exch_rate = get_currency('XRP')
print(btc_exch_rate['data']['rates']['USD'])
