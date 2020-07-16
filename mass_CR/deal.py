import pandas as pd
import numpy as np

from pylab import mpl  # 中文图例
import matplotlib.pyplot as plt
mpl.rcParams['font.sans-serif'] = ['SimHei']  # SimHei是黑体的意思
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
import statsmodels.api as sm
from WindPy import w
#w.start()


if __name__ == '__main__':
    data = pd.read_excel("50增强策略.xlsx")
    print(data)

    for i in range(1,len(data)):
        data.loc[i, 'PNL'] = data.loc[i, 'cash'] - data.loc[i-1, 'cash']
    data.to_excel("50增强策略.xlsx", index=False)