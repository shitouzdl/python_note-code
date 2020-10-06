import pandas as pd

def age_18_to_30(a):
    return 18 <= a < 30

def level_a(s):
    return 85 <= s <= 100

students = pd.read_excel("C:/Users/18736/Desktop/pandas/008/Students.xlsx",index_col="ID")
# students = students.loc[students['Age'].apply(age_18_to_30)].loc[students['Score'].apply(level_a)]
students = students.loc[students.Age.apply(age_18_to_30)].loc[students.Score.apply(level_a)]
# 方法二
# students = students.loc[students.Age.apply(lambda a: 18 <= a < 30)] \
#     .loc[students.Score.apply(lambda s: 85 <= s <= 100)]
# 折行方法 空格 ＋ \  使用12，13行的lambda方法 需要注释掉def
# 注意：loc[],apply(),students[] 使用的括号
# students是一个dateframe类型，loc[]之后的一列是series类型，都要用方括号表明类型
# apply()方法 表示将前面的一列数据塞进函数中进行筛选，满足条件保留，不满足过滤掉
print (students)