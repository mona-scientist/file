import time
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


import statsmodels.api as sm
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.stattools import adfuller

pd.options.display.max_columns = 99
plt.rcParams['figure.figsize'] = (12, 8)
df_train = pd.read_csv('train.csv', parse_dates=['date'], index_col=['date'])
df_test = pd.read_csv('test.csv', parse_dates=['date'], index_col=['date'])
df_train.shape, df_test.shape
