import pandas as pd
import matplotlib.pyplot as plt
users = pd.read_excel('C:/Users/18736/Desktop/pandas/011/Users.xlsx')

users['total'] = users['Oct']+users['Nov']+users['Dec']  # 排序用
users.sort_values(by='total', inplace=True, ascending=True)
# print(users)
# users.plot.bar(x='Name', y=['Oct', 'Nov', 'Dec'],
#                stacked=True, title='User Bahavior')
users.plot.barh(x='Name', y=['Oct', 'Nov', 'Dec'],
               stacked=True, title='User Bahavior')
plt.tight_layout()
plt.show()
