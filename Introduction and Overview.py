import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df= pd.read_csv('D:\education\ML\Introduction of PR\Introduction-of-PR\Housing.csv')

X=df.iloc[:, 3].values

y=df.iloc[:, 6].values

plt.plot(X, y, '.r')
plt.xlabel('bedrooms')
plt.ylabel('sqft_lot')
plt.show()