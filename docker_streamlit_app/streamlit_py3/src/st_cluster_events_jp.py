# covid19データ・セットダウンロード、カラム名を変更して保存
# 情報源: 厚労省
# データ・セット
# DATA_URL = 'https://covid19.mhlw.go.jp/public/opendata/cluster_events_weekly.csv'

# ライブラリ・インポート
import os
import pandas as pd
import plotly.express as px
import streamlit as st
import datetime

# データ・セット読み込み
# DATA_URL = 'https://covid19.mhlw.go.jp/public/opendata/cluster_events_weekly.csv'
# RAW_DATA = pd.read_csv(DATA_URL)

DATA_DIR = './data/'
# DATA = 'latest_cluster_events.csv'
# df = pd.read_csv(os.path.join(DATA_DIR, DATA), index_col=[0])

CL_DATA = pd.read_csv(os.path.join(DATA_DIR, 'cluster_events_weekly.csv'))

df = CL_DATA

# クラスターイベントのカラム名修正
df = df.rename(columns={'Medical institutions': 'MedicalInstitutions'})
df = df.rename(columns={'Welfare facilities': 'Welfare_facilities'})
df = df.rename(columns={'(For the elderly)': 'FacilitiesFortheElderly'})
df = df.rename(columns={'(For children)': 'FacilitiesForChildren'})
df = df.rename(columns={'(For persons with disabilities)': 'FacilitiesForDisabilities'})
df = df.rename(columns={'Sports facilities, etc.': 'FacilitiesForSports'})
df = df.rename(columns={'Schools,  etc.': 'SchoolsEtc'})
df = df.rename(columns={'Companies, etc.': 'Companies'})

df = df.drop(columns={'Week', 'Prefecture'})

# 転置
df = df.T
# df = df.reset_index()

# 全国の最終週のクラスター発生状況
# [2021/07/26~2021/08/01]
df = pd.DataFrame(df[2])

# df = df.reset_index()
df = df.rename(columns={2 :'case'}) 
# df = df.set_axis({'cluster_events', 'case'}, axis=1)
# df = df.set_axis({'cluster_events'}, axis=1)

# plot
st.header('国内のクラスター発生状況')
st.write('情報源: データからわかる－新型コロナウイルス感染症情報－')
st.write('期間: 2021/07/26~2021/08/01')

st.write(
    px.bar(data_frame=df, title='最終週のクラスター発生状況')
 )

