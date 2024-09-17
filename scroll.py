import pandas
import numpy

data = pandas.read_csv('./scrollMarks.csv')


b = data['marks'].sum()
c = data['marks'].median()

# marks 的总量
# print(f'{b}') 

# marks 的中位数
# print(f'{c}')

d = data[data['marks'] < c]

# marks 小于中位数的地址
# print(f'{d}')

e = data[data['marks'] > c]
# marks 大于中位数的地址
# print(f'{e}')

g = data[data['marks'] < 100]

# marks 小于 100 的地址
# print(f'{g}')

h = data[data['marks'].map(lambda x: x > 100 and x < c)]
# marks 大于 100 和小于中位数的地址
print(f'{h}')