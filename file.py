import os
import json
import pandas

# print(f'{__file__}')
# print(f'{__doc__}')
# print(f'{__name__}')

# cur_path = os.path.dirname(__file__)

# print(f'{cur_path}')

# f = open('./test.json', 'r')
# j = f.read()
# f.close()

# print(f'{j}')

# t = json.loads(j)
# name = t['name']

# print(f'{name}')

# t['price'] = 12000

# text = json.dumps(t)

# w = open('./test.json', 'w')
# w.write(text)
# w.close()

data = pandas.read_csv('./test.csv')

print(f'{data.columns}')
print(f'{data.head(10)}')
