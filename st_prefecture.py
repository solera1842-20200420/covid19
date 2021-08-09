# 県別の感染状況
# 県別の週次データをプロット
# ライブラリ・インポート
import os
import pandas as pd
# import matplotlib.pyplot as plt
import plotly.express as px
import streamlit as st

# import seaborn as sns
# %matplotlib inline

# csv読み込み
DATA_DIR = './data/mhlw/'

# 週次データ
RAW_DATA = 'newcases_detail_weekly.csv'

# データ読み込み
def weekly_data():
    df = pd.read_csv(os.path.join(DATA_DIR, RAW_DATA))
    return df

# 欠損値処理
def data_fill_na():
    df = weekly_data()
    df = df.replace({'*': 0})
    return df

# データ型変換
def data_cast():
    df = data_fill_na()
    df = df.astype({'Male Under 10': int, 'Male 10s': int, 'Male 20s': int, 'Male 30s': int, 'Male 40s': int,
                    'Male 50s': int, 'Male 60s': int, 'Male 70s': int, 'Male 80s': int, 'Male Over 90': int,
                    'Female Under 10': int, 'Female 10s': int, 'Female 20s': int, 'Female 30s': int, 'Female 40s': int,
                    'Female 50s': int, 'Female 60s': int, 'Female 70s': int, 'Female 80s': int, 'Female Over 90': int})
    return df

# 県別にデータ加工
def prefecture_data():
    # 性別・年代別新規陽性者(週次)
    # df = weekly_data()
    # df = data_fill_na()
    df = data_cast()
    # df = pd.read_csv(DATA_DIR + 'newcases_detail_latest.csv', index_col=[0])

    df = df.drop(columns={'Week'})
    df = df.query('Prefecture != "ALL"')
    df = df.replace({'*': 0})
    return df

df_prefecture = prefecture_data()
df_prefecture_melt = df_prefecture.melt(id_vars="Prefecture", value_name="case")
df_prefecture_melt.sort_values('Prefecture')

# plot
st.write(
    px.bar(data_frame=df_prefecture_melt, x="Prefecture", y="case", title="最終週県別の感染者数")
)

st.write(
    px.box(data_frame=df_prefecture_melt.sort_values('Prefecture'), x="Prefecture", y="case", title="最終週の県別boxplot")
)