import numpy as np        # 用公式產生資料點(有已知資料就不需要)
import matplotlib.pyplot as plt # 繪圖用
import pandas as pd
import json

from matplotlib.font_manager import fontManager, FontProperties

# 根據字型名稱，設定matplotlib的字型
from matplotlib import rc
rc('font', family='Taipei Sans TC Beta')
plt.rcParams['axes.unicode_minus'] = False

import requests
url = 'https://ws.kinmen.gov.tw/001/Upload/0/relfile/0/0/5bd6c919-c0f6-44bf-a047-fd6e22645bcd.json'
data = requests.get(url)   # 使用 get 方法
data_json = data.json()

print(pd.DataFrame(data.items()))