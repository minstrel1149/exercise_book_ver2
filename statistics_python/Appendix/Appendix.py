import numpy as np

height = np.array([181,161,170,160,158,168,162,179,183,178])
height
weight = np.array([78,49,52,53,50,57,53,54,71,73])
weight

BMI = weight / ( height / 100 )**2
BMI

import matplotlib.pyplot as plt

plt.scatter(height, weight)


import pandas as pd

df = pd.read_csv('C:\\Users\\inha\\Desktop\\BMI-example.txt',sep = '\t',header=None)
df
height = np.array(df[0])
weight = np.array(df[1])
height
weight
