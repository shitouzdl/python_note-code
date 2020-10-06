import pandas as pd
import matplotlib.pyplot as plt
students = pd.read_excel('C:/Users/18736/Desktop/pandas/009/Students.xlsx')
students.sort_values(by='Number',inplace=True,ascending=False)  #不加inplace=true 可以试一下 没有变化
print(students)
plt.bar(students.Field,students.Number,color='orange')
plt.xticks(students.Field,rotation=90)
plt.xlabel('Field')
plt.ylabel('Number')
plt.title('International Students By Field',fontsize=16)
plt.tight_layout()
plt.show()