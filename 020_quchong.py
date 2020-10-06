import pandas as pd
students = pd.read_excel(
    'C:/Users/18736/Desktop/pandas/020/Students_Duplicates.xlsx')
# students.drop_duplicates(subset='Name',inplace=True,keep='last')
# print(students)
# 去重
dupe = students.duplicated(subset='Name')
dupe = dupe[dupe == True]
# print(dupe)
# print(dupe.index) 筛选出重复值，定位到重复值
print(students.iloc[dupe.index])