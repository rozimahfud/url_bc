import pandas as pd
import numpy as np

dataset = pd.read_csv('/home/es5research/Documents/dataset/URL/urldataset/data.csv')

good_data = dataset[dataset['label']=='bad']
print(good_data)
