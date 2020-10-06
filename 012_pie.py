import pandas as pd
import matplotlib.pyplot as plt
students = pd.read_excel(
    'C:/Users/18736/Desktop/pandas/012/Students.xlsx', index_col='From')
# students.sort_values(by='2017',inplace=True)
students['2017'].sort_values().plot.pie(fontsize=8, counterclock=False)
# sort_values两种写法 参数startangle=-270改变起始角度，但是默认的排版好看
plt.title('Source Of International Students', fontsize=16, fontweight='bold')
plt.ylabel('2017', fontsize=6, fontweight='bold')
# 方括号和 .---- 使用起来一样，但是这里是2017数字，必须使用方括号，字母都可以使用
# print(students)
plt.show()
