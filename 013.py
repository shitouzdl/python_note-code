import pandas as pd
import matplotlib.pyplot as plt
weeks = pd.read_excel('C:/Users/18736/Desktop/pandas/013/Orders.xlsx', index_col='Week')
print(weeks)
print(weeks.columns)
weeks.plot.area(y=['Accessories', 'Bikes', 'Clothing', 'Components']) #加area绘制的是叠加图 不加默认绘制折线图
# 叠加柱状图重在表达在某个节点，数据的高度；叠加区域图指明趋势，淡季旺季在连续趋势中容易查看
plt.title('sale',fontsize = 18,fontweight = 'bold')
plt.ylabel('Total',fontsize = 12,fontweight = 'bold')
plt.xticks(weeks.index,fontsize = 8)
plt.show()