import requests

def get_my_portfolio():
  return {'BTC': 1, 'ETH': 10, 'SOL': 100}

def statistics():
  my_portfoli = get_my_portfolio()
  tickers = ['BTCUSDT', 'ETHUSDT', 'SOLUSDT']
  portfolio = {'BTC': 0, 'ETH': 0, 'SOL': 0}

  for ticker in tickers:
    url = 'https://api1.binance.com/api/v3/ticker/price?symbol=' + ticker
    print(f'{url}')
    r = requests.get(url)
    j = r.json()
    price = float(j['price'])
    if ticker == 'BTCUSDT':
      btc = my_portfoli['BTC'] * price
      portfolio['BTC'] = btc
    elif ticker == 'ETHUSDT':
      eth = my_portfoli['ETH'] * price
      portfolio['ETH'] = eth
    else:
      sol = my_portfoli['SOL'] * price
      portfolio['SOL'] = sol

  print(f'{portfolio}')
  
statistics()