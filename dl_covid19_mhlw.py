#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 12:52:07 2021
情報源: 厚労省オープンデータ
https://covid19.mhlw.go.jp/

データからわかる－新型コロナウイルス感染症情報
https://www.mhlw.go.jp/stf/covid-19/open-data.html

@author: nk
"""

# import library
import pandas as pd

# データ保存先
data_dir = './data/'
mhlw_dir = (data_dir + 'mhlw/')

# データのダウンロード・保存
# PCR検査実施者数
print('PCR検査実施者数')
df_tests_daily = pd.read_csv(
 'https://www.mhlw.go.jp/content/pcr_tested_daily.csv')
df_tests_daily.to_csv(mhlw_dir + 'pcr_tested_daily.csv', index=False)

# 陽性者数(デイリー)
print('陽性者数(デイリー)')
df_positive_daily = pd.read_csv(
 'https://www.mhlw.go.jp/content/pcr_positive_daily.csv')
df_positive_daily.to_csv(mhlw_dir + 'pcr_positive_daily.csv', index=False)

# 退院者数(累積)
print('退院者数(累積)')
df_recovered_total = pd.read_csv(
 'https://www.mhlw.go.jp/content/recovery_total.csv')
df_recovered_total.to_csv(mhlw_dir + 'recovery_total.csv', index=False)

# 死亡者数(累積)
print('死亡者数(累積)')
df_deaths_total = pd.read_csv(
 'https://www.mhlw.go.jp/content/death_total.csv')
df_deaths_total_daily = pd.read_csv(
 'https://covid19.mhlw.go.jp/public/opendata/deaths_cumulative_daily.csv')
df_deaths_total_daily.to_csv(mhlw_dir + 'deaths_cumulative_daily.csv', index=False)

# 新規感染者(県別)
print('新規感染者(県別)')
df_newcases_daily = pd.read_csv('https://covid19.mhlw.go.jp/public/opendata/newly_confirmed_cases_daily.csv')
df_newcases_daily.to_csv('./data/mhlw/newly_confirmed_cases_daily.csv', index=False)

# 人口10万人あたり新規陽性者数
print('人口10万人あたり新規陽性者数')
df_100k_cases_daily = pd.read_csv('https://covid19.mhlw.go.jp/public/opendata/newly_confirmed_cases_per_100_thousand_population_daily.csv')
df_100k_cases_daily.to_csv('./data/mhlw/newcases_per_100k_daily.csv', index=False)

# 性別・年代別新規陽性者(週次)
print('性別・年代別新規陽性者(週次)')
df_new_cases_detail_weekly = pd.read_csv('https://covid19.mhlw.go.jp/public/opendata/newly_confirmed_cases_detail_weekly.csv')
df_new_cases_detail_weekly.to_csv('./data/mhlw/newcases_detail_weekly.csv', index=False)

# 陽性者数(累積)
print('陽性者数(累積)')
df_cases_total_daily = pd.read_csv('https://covid19.mhlw.go.jp/public/opendata/confirmed_cases_cumulative_daily.csv')
df_cases_total_daily.to_csv('./data/mhlw/confirmed_cases_cumulative_daily.csv', index=False)

# 重症者数の推移
print('重症者数の推移')
df_severe_daily = pd.read_csv('https://covid19.mhlw.go.jp/public/opendata/severe_cases_daily.csv')
df_severe_daily.to_csv('./data/mhlw/severe_cases_daily.csv', index=False)

# 要治療者数
print('要治療者数')
df_patient_daily = pd.read_csv('https://covid19.mhlw.go.jp/public/opendata/requiring_inpatient_care_etc_daily.csv')
df_patient_daily.to_csv('./data/mhlw/requiring_inpatient_daily.csv', index=False)

# 死亡者数の累積
print('死亡者数の累積')
df_deaths_total_daily = pd.read_csv('https://covid19.mhlw.go.jp/public/opendata/deaths_cumulative_daily.csv')
df_deaths_total_daily.to_csv(mhlw_dir + 'deaths_cumulative_daily.csv', index=False)

print('Script End..')
# end...
