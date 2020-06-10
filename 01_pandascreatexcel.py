import pandas as pd
df = pd.DataFrame({'id':[1,2,3],'name':['tim','mike','victor']})
df = df.set_index('id')
print(df)
df.to_excel('C:/output.xlsx')
print('done!')
