# 東京都内のcovid19 EDA

# ライブラリ・インポート
import pandas as pd
import streamlit as st
import plotly.express as px

# データ・セットの読み込み
data_dir = './data/covid19_tokyo/'
dataset = 'covid19_tokyo_job.csv'

df = pd.read_csv(data_dir + dataset)

# plot
st.write(
    px.bar(data_frame=df, x='occupation', y='cases_cumulative',
           title='職業別感染状況(累積)【東京都内】')
)
