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
DATA_SET = '130001_tokyo_covid19_patients.csv'

# データのダウンロード
print('データのダウンロード: "https://stopcovid19.metro.tokyo.lg.jp/data/130001_tokyo_covid19_patients.csv"')
DATA_URL = 'https://stopcovid19.metro.tokyo.lg.jp/data/130001_tokyo_covid19_patients.csv'
df = pd.read_csv(DATA_URL)

# csvの書き込み
print('東京都のcovid19の感染情報ダウンロード・'書き込み')
df.to_csv(DATA_DIR + DATA_SET)
