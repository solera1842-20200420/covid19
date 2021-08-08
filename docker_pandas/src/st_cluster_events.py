# covid19クラスター発生状況
# データからわかる－新型コロナウイルス感染症情報
# https://covid19.mhlw.go.jp/?lang=ja
# データセット: 'https://covid19.mhlw.go.jp/public/opendata/cluster_events_weekly.csv'

DATA_URL = 'https://covid19.mhlw.go.jp/public/opendata/cluster_events_weekly.csv'

# ライブラリ
import os
import pandas as pd
import plotly.express as px
import streamlit as st
# import seaborn as sns

# データ・セット
RAW_DATA = pd.read_csv(os.path.join(DATA_URL))

# 直近のクラスター発生状況
df = RAW_DATA.drop(columns={"Total", "Prefecture"})

# 最終週のデータを抽出、転置
df_weekly = df.tail(1).T
df_weekly = df_weekly.drop(index={'Week'})

# plot用データ作成
df_weekly = df_weekly.reset_index()
df_weekly =df_weekly.set_axis(['ClusterEvents', 'Newly_Confirmed_Cases'], axis=1)

# plot
st.write(
	px.bar(data_frame=df_weekly, x='ClusterEvents', y="Newly_Confirmed_Cases", title="最終週のクラスター発生状況")
)
