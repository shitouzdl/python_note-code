import pandas as pd
import numpy as np
orders = pd.read_excel(
    'C:/Users/18736/Desktop/pandas/023/Orders.xlsx')
orders['Year'] = pd.DatetimeIndex(orders['Date']).year
pt1 = orders.pivot_table(index='Category', columns='Year',
                         values='Total', aggfunc=np.sum) #每一项和excel透视表的项目对应
print(pt1)
