import pandas as pd
import matplotlib.pyplot as plt
homes = pd.read_excel('C:/Users/18736/Desktop/pandas/014/home_data.xlsx')
print(homes.corr())