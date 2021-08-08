# covid19 data hubからデータのダウンロード
# ライブラリのインポート
from covid19dh import covid19
import os
import pandas as pdb

# x, src = covid19()
# x, src = covid19("USA") # Unites States
x, src = covid19("JPN") # Jaapan

# データ保存先ディレクトリ
DATA_DIR = './data/'

# csv書き込み
print('covid19_data_hubの日本のデータ書き込み')
x.to_csv(os.path.join(DATA_DIR, 'covid19dh_jpn.csv'))
print('covid19_data_hubからの日本のデータの情報源の書き込み')
src.to_csv(os.path.join(DATA_DIR, 'covid19dh_jpn_src.csv'))
