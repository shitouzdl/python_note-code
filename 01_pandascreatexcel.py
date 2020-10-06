import pandas as pd
df = pd.DataFrame({'id':[1,2,3],'name':['tim','mike','victor']})
df = df.set_index('id')
print(df)
df.to_excel('C:/Users/18736/Desktop/pandas/output.xlsx')
print('done!')