import pandas as pd
import matplotlib.pyplot as plt
homes = pd.read_excel('C:/Users/18736/Desktop/pandas/014/home_data.xlsx')
# print(homes.head())
# homes.sqft_living.plot.hist(bins=100)
# plt.xticks(range(0, max(homes.sqft_living), 500), fontsize=8, rotation=90) 
#直方图 rotation 旋转角度
homes.sqft_living.plot.kde()
plt.xticks(range(0, max(homes.sqft_living), 500), fontsize=8, rotation=90)
plt.show()
