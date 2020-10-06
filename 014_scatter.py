# 散点图，直方图，密度图
import pandas as pd
import matplotlib.pyplot as plt
homes = pd.read_excel('C:/Users/18736/Desktop/pandas/014/home_data.xlsx')
# print(homes.head())
homes.plot.scatter(y='sqft_living',x='price')
plt.show()