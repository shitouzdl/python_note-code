import pandas as pd
books = pd.read_excel('C:/Users/18736/Desktop/pandas/006/Books.xlsx', index_col='ID')
#知识点1
# books['Price'] = books['ListPrice'] * books['Discount']
#在excel中操作的是单元格 在pandas中操作的是列 [] 也说明了对列操作
#知识点2
# for i in books.index:    #获取index整列的数字
# for i in range(5, 15):    #获取5-14的数字
    # books['Price'].at[i] = books['ListPrice'].at[i] * books['Discount'].at[i]
# 知识点3 ListPrice 加 2   或者使用定义函数 def add_2(x): return x + 2 下面使用apply(add_2)
books['ListPrice'] = books['ListPrice'].apply(lambda x: x + 2)
print(books)