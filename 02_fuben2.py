import pandas as pd
people = pd.read_excel('C:/Users/18736/Desktop/pandas/002/People_fuben2.xlsx',index_col='ID')
people.to_excel('C:/Users/18736/Desktop/pandas/002/People_fuben3.xlsx')
print('done!')