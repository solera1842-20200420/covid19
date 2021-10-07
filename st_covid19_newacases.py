"""
Plot Covid19 NewCases in Japan
"""

# starandard libarary
import datetime as dt
import numpy as np
import os
import pandas as pd
# import pandas_datareader as pdr

# for plot
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objs as go
import plotly.figure_factory as ff
from plotly.subplots import make_subplots
import seaborn as sns
import streamlit as st

# for ml, statistics
import statsmodels.api as sm
import statsmodels.formula.api as smf
#from statsmodels.tsa import seasonal

# dataset
DATA_DIR ='./data/mhlw'
RAW_DATA = 'newly_confirmed_cases_daily.csv'
@st.cache
def load_dataset():
    df = pd.read_csv(os.path.join(DATA_DIR, RAW_DATA))  # read csv
    return df

# daily data in japan
def data_jp():
    df = load_dataset()
    df = df.query('Prefecture == "ALL"')  # exclude data each prefecture
    df = df.rename(columns={'Newly confirmed cases': 'NewCases'})  # rename column
    df = df.drop(columns={'Prefecture'})
    return df

# daily data in 7days
def last_7days():  # last 7days
    df = data_jp()
    df = df.tail(7)
    return df

# function: trend
# 14days
def get_trend14():
    df = data_jp()
    d_newcases = df['NewCases'].astype(float)
    stl_14 = sm.tsa.seasonal_decompose(d_newcases, period=14)
    trend_14 = stl_14.trend
    return trend_14

# 60dyas
def get_trend60():
    df = data_jp()
    d_newcases = df['NewCases'].astype(float)
    stl_60 = sm.tsa.seasonal_decompose(d_newcases, period=60)
    trend_60 = stl_60.trend
    return trend_60

"""
# fuction: plot dailydata
def plot_ts():
    df = data_jp()
    plot_line = px.line(data_frame=df, x=df['Date'], y=df['NewCases'], title="NewCasesInJapan")
    return plot_line
"""

# funtion: plot rate of change
def plot_PctChange():
    df = data_jp()
    plot_line = px.line(data_frame=df, x=df['Date'], y=df['NewCases'].pct_change(), title="RateOfChangeFromPreviousDay")
    return plot_line

# function: plot daily data and sma
def plot_sma():
    df = data_jp()
    fig_SMA = make_subplots(rows=1, cols=1, specs=[[{'secondary_y': True}]])
    fig_SMA.add_trace(go.Scatter(x=df['Date'],
                                 y=df['NewCases'],  # daily data
                                 name="Daily"))
    fig_SMA.add_trace(go.Scatter(x=df['Date'],
                                 y=df['NewCases'].rolling(14).mean(),  # SMA14days
                                 name="SMA: 14days"))
    fig_SMA.add_trace(go.Scatter(x=df['Date'],
                                      y=df['NewCases'].rolling(30).mean(),  # SMA30days
                                      name="SMA: 30days"))
    fig_SMA.add_trace(go.Scatter(x=df['Date'],
                                 y=df['NewCases'].rolling(60).mean(),  # SMA60days
                                 name="SMA: 60days"))

    fig_SMA.update_layout(title_text="NewlyConfirmedCasesInJapan: Daily, 14days, 30days, 60days'",
                          width=900, height=400)
    return fig_SMA

# function: plot trend
def plot_trend():
    trend_14 = get_trend14()
    trend_60 = get_trend60()
    fig_trend = make_subplots(rows=1, cols=1, specs=[[{'secondary_y': True}]])
    fig_trend.add_trace(go.Scatter(x=trend_14.index, y=trend_14, name="Trend: 14days"))
    fig_trend.add_trace(go.Scatter(x=trend_60.index, y=trend_60, name="Trend: 60days"))
    fig_trend.update_layout(title_text="TrendInJapan: 14days, 60days'",
                          width=900, height=400)
    return fig_trend

"""
Display Dataframe and Plot
"""
st.write(
    last_7days()
)

st.write('時系列データをline plot')
# plot_ts()
print("Date:", dt.datetime.today())

# plot sma
st.write(
    plot_sma()
)

# plot trend
st.write(
    plot_trend()
)

# plot rate of change
st.write(
    plot_PctChange()
)

# scipt end...