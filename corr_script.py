import pandas as pd
import matplotlib.pyplot as plt
df_driver_b = pd.read_csv('DRIVER_B.csv')

#print(df_driver_b.head())

plt.matshow(df_driver_b.corr())
plt.savefig('test.png')