### BITCOIN PRICE ORACLE #################################################################

'''
API URLS:
    BITSTAMP
        Some coins and currencies
        https://www.bitstamp.net/api/
        https://www.bitstamp.net/api/ticker/
        100% free !!

    CRYPTOWAT.CH
        multiple exchanges !!!
        https://cryptowat.ch/products/cryptocurrency-market-data-api
        https://docs.cryptowat.ch/rest-api/
        https://api.cryptowat.ch/markets/kraken/btcusd/price  (limited but should suffice : 2 to 4 calls/minute)

    COINBASE
        https://developers.coinbase.com/docs/wallet/guides/price-data
        https://api.coinbase.com/v2/prices/spot?currency=USD

    COINGECKO
        https://www.coingecko.com/api/documentations/v3#/
        https://api.coingecko.com/api/v3/ping
        https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd
        limit 100 req/minute

    CEX.IO
        https://cex.io/api/ticker/BTC/USD
        https://cex.io/api/last_price/BTC/USD

    THEROCK
        Limit one every 2 seconds
        https://api.therocktrading.com/v1/funds/BTCEUR/ticker


    ### Second Choices ###

    COINAPI.IO
        https://www.coinapi.io/         (100 free reqs per day = 1 call every 15m)
    
    BLOCKCHAIN.INFO
        https://www.blockchain.com/it/api/exchange_rates_api
        https://blockchain.info/ticker      (Updates every 15 min (price is "old"))
    
    COINMARKETCAP
        costs and limits
        https://coinmarketcap.com/api/documentation/v1/     (10K call/mo (1 call every 4.32 min))
        non commercial use

    CRYPTOCOMPARE
        requires api-key
        https://min-api.cryptocompare.com       (up to 50 calls/sec !!)
        https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD
        non commercial use

'''
##########################################################################################

import requests
import sys

### Selected API Calls ##############################################################   Json response fields

'''
    SELECTED:
    https://cex.io/api/last_price/BTC/USD                                           /   lprice
    https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd     /   bitcoin,usd
    https://api.cryptowat.ch/markets/kraken/btcusd/price                            /   result,price
    https://www.bitstamp.net/api/ticker/                                            /   last
'''




##########################################################################################


def update_price(value, samples, mode):
    ''' 
    make a tx to the SC Oracle with:
    - value = measured value
    - samples = number of samples used to measure
    - mode = type of measurement
    - unixtimestamp (might differ from block time)
    '''
    pass 

### Averages and other values extraction #################################################

def maxValue(values):
    return max(values)

def minValue(values):
    return min(values)

def simpleAverage(values):
    return round(sum(values)/len(values),4)

def weightedAverage(values):
    values.remove(min(values))
    values.remove(max(values))
    return simpleAverage(values)

def get_price(proces):
    '''
    Get the value as a proces on the values read from the different sources
        get as a param the name of the function that will extract the value
        from the array of sample
    '''
    values = []
    value = 0
    samples = 0

    # get each sample price here
    for call in urlList:
        url=call[0]
        key = call[1]
        response = requests.get(url)
        json = response.json()
        #print(f" call {url} - value {json} - keys {key}")
        if len(key) == 2:
            values.append(float(json[key[0]][key[1]]))
        else :
            values.append(float(json[key]))
    
    # print(f"Res : {values}")
    # print(maxValue(values))
    # print(minValue(values))
    # print(simpleAverage(values))
    # print(weightedAverage(values))
    
    samples = len(urlList)
    value = proces(values)
    
    return (value, samples)


def main():
    ''' The main steps '''
    
    value = 0           # float: the bitcoin price 
    samples = 0         # int : number of samples taken to determine price


    # get the price and measurements using the given processing function
    (value, samples) = get_price(mode)
    print(f"value : {value} - samples {samples} - method {mode.__name__}" )

    # make tx
    update_price(value, samples, mode.__name__)


### GLOBALS / CONFIGURATION ##############################################################

# list of tuples that define the sources of the information
urlList = [
    ("https://cex.io/api/last_price/BTC/USD", ("lprice")),
    ("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd", ("bitcoin","usd")),
    ("https://api.cryptowat.ch/markets/kraken/btcusd/price",("result","price")),
    ("https://www.bitstamp.net/api/ticker/",("last"))
]

# mode = function name of the function used to process data :
# (maxValue, minValue, simpleAverage, weightedAverage)
mode = weightedAverage


### START ################################################################################

if sys.version_info[0] < 3:
    print("Please use python3")
    sys.exit()

if __name__ == "__main__":
    main()