import pandas as pd
people = pd.read_excel('C:/Users/18736/Desktop/pandas/002/People.xlsx')
print (people.shape)
print (people.columns)
print (people.head(3))
print('=======================')
print(people.tail(3))