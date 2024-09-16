import pandas

addresses = [
  '0x00035ab46994cda43f150b2be16bb7ca423171c7'
]

data = pandas.read_csv('./eliminatedSybilAttackers.csv')
result = data['address'].isin(addresses)

if result.any():
  print('在女巫列表')
else:
  print('不在女巫列表')