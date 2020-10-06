import pandas as pd
students = pd.read_excel(
    'C:/Users/18736/Desktop/pandas/016/Student_score.xlsx', sheet_name='Students')
scores = pd.read_excel(
    'C:/Users/18736/Desktop/pandas/016/Student_score.xlsx', sheet_name='Scores')
table = students.merge(scores,how='left', on='ID').fillna(0)  # 加left保留左边的数据
table.Score = table.Score.astype(int)
print(table)
