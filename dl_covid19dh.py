# covid19 data hubからデータのダウンロード
# ライブラリのインポート
from covid19dh import covid19
import pandas as pd

# x, src = covid19()
# x, src = covid19("USA") # Unites States
x, src = covid19("JPN") # Jaapan

# データ保存先ディレクトリ
data_dir = './data/'

# csv書き込み
print('covid19_data_hubの日本のデータ書き込み')
x.to_csv(data_dir + 'covid19dh_jpn.csv', index=False)
print('covid19_data_hubからの日本のデータの情報園の書き込み')
src.to_csv(data_dir + 'covid19dh_jpn_src.csv', index=False)

