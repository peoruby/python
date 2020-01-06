########
#https://api.coindesk.com/v1/bpi/currentprice/USD.json
#ref: https://pypi.org/project/requests/
#######
import requests

def getBTCUSD():
    api = "https://api.coindesk.com/v1/bpi/currentprice/USD.json"
    ret = requests.get(api)
    if ret.status_code == 200:
        ret = ret.json()
        btc_price = ret['bpi']['USD']['rate']
        for x in range(5):
            print(str(x+1) + ": " + btc_price)
    else:
        print("Unable to call API this time.")
        return False
if __name__ == '__main__':
    print(getBTCUSD())