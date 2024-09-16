import requests


r = requests.get('https://api1.binance.com/api/v3/ticker/price?symbol=ETHUSDT')
j = r.json()


print(f'{j}')