# covid19データ・セットダウンロード(東京都)
# 情報源：　https://catalog.data.metro.tokyo.lg.jp
# データ・セット: https://stopcovid19.metro.tokyo.lg.jp/data/130001_tokyo_covid19_patients.csv

# ライブラリ・インポート
import numpy as np
import pandas as pd
# import plotly.express as px
# import matplotlib.pyplot as plt
#import japanize_matplotlib
# import seaborn as sns

# データ・セット保存先ディレクトリとファイル名
data_dir = './data/covid19_tokyo/'
dataset = '130001_tokyo_covid19_patients.csv'

# データのダウンロード
print('データのダウンロード: "https://stopcovid19.metro.tokyo.lg.jp/data/130001_tokyo_covid19_patients.csv"')
data = 'https://stopcovid19.metro.tokyo.lg.jp/data/130001_tokyo_covid19_patients.csv'
df = pd.read_csv(data)

# csvの書き込み
df.to_csv(data_dir + dataset)
