import pandas as pd
import matplotlib.pyplot as plt
students = pd.read_excel('C:/Users/18736/Desktop/pandas/009/Students.xlsx')
students.sort_values(by='Number',inplace=True,ascending=False)  #不加inplace=true 可以试一下 没有变化
print(students)
students.plot.bar(x='Field',y='Number',color='orange',title='international students by Field')
plt.tight_layout()
plt.show()