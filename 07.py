import pandas as pd
products = pd.read_excel('C:/Users/18736/Desktop/pandas/007/List.xlsx',index_col='ID')
products.sort_values(by=['Worthy','Price'],inplace=True,ascending=[True,False])
#使用inplace当前的dataframe排序而不是新建立dateframe
#当有两个排序条件时，将条件放入一个list中 []，排序方法前后对应list
print(products)