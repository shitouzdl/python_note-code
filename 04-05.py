import pandas as pd
from datetime import date, timedelta

def add_month(d, md):
    yd = md // 12
    m = d.month + md % 12
    if m != 12:
        yd += m // 12
        m =m % 12
    return date(d.year + yd, m, d.day)    #增加月份的算法

books = pd.read_excel('C:/Users/18736/Desktop/pandas/004/Books.xlsx',skiprows=3,usecols="C:F",index_col=None,dtype={'ID':str,'InStore':str,'Date':str})
# print(type(books['ID']))    #这里print ID，要用方括号 使ID整列变为series
# books['ID'].at[0] = 100    #学习快速填充，这行是实现填充一行的方法
start = date(2020, 1, 1)
for i in books.index:    #如果只填写index 提示没有定义
    books['ID'].at[i] = i + 1
    books['InStore'].at[i] = 'Yes' if i % 2 == 0 else 'No'
    # books['Date'].at[i] = start + timedelta(days = i)    #增加天数
    # books['Date'].at[i] = date(start.year + i, start.month, start.day)    #增加年
    books['Date'].at[i] = add_month(start, i)
books.set_index('ID',inplace=True)
books.to_excel('C:/Users/18736/Desktop/pandas/004/output.xlsx')
print('Done!')