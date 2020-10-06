import pandas as pd
employees = pd.read_excel(
    'C:/Users/18736/Desktop/pandas/018/Employees.xlsx', index_col='ID')
df = employees['Full Name'].str.split(expand=True)
employees['First Name'] = df[0]
employees['Last Name'] = df[0]
print(employees)
