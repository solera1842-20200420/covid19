#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 15:30:04 2021
データフレームの可視化
dataset: 厚労省
@author: nk
"""
# import library
import os
import pandas as pd
import streamlit as st
import plotly.express as px

# データ・セットの読み込み
# 情報源: 厚労省オープンデータ

DATA_DIR = './'

# 陽性者数(デイリー)
DATA = pd.read_csv(os.path.join(DATA_DIR, 'newly_confirmed_cases_daily.csv'))

# 県別のデータ削除
def select_data():
    df = DATA.query('Prefecture == "ALL"')
    return df

# 県名のカラム(Prefecture)削除
def data_ts():
    df = select_data()
    return df

# カラム名変更
def mk_plotdata():
    df = data_ts()
    df = df.rename(columns={'Newly confirmed cases':'NewCases'})
    return df

# 時系列データplot
df = mk_plotdata()
st.write(
	px.bar(data_frame=df, x="Date", y="NewCases", title="全国の日別感染状況")
)

# df
# script end...
