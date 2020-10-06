import pandas as pd


def score_validation(row):
    try:
        assert 0 <= row.Score <= 100
    except:
        print(f'#{row.ID}\tstudent {row.Name} has an invalid score {row.Score}')


students = pd.read_excel('C:/Users/18736/Desktop/pandas/017/Students.xlsx')
# print(students)
students.apply(score_validation, axis=1)  # 0从上到下 1从左到右
