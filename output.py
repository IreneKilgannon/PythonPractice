import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

iris = pd.read_csv("irisdata.csv", header = None)

head = f'The first five rows of the data set are: \n {iris.head()}'

with open('analysis.txt', 'wt') as f:
    f.write(head)
