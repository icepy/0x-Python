print("Hello icepy.eth")

cex_markets = {'BTC': 60000, 'ETH': 2400}
dex_markets = [59888, 59990, 60200]

def get_price(token_name):
  price = cex_markets[token_name]
  return price

def arbitrage(price):
  spread = 0
  for tic in dex_markets:
    if tic < price:
      continue
    else:
      spread = tic - price
      break
  
  print(f'利差：{spread}')    


cex_price = get_price('BTC')
arbitrage(cex_price)
