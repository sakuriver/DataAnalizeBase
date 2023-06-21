# -*- coding: utf-8 -*-
import plotly.express as px
import pandas as pd
import csv

# DAU(折れ線グラフ)
# データ構造.
# 日付  ラベル.
#データ軸 dauの数.
labelkeys = []
datas = []
with open("./sample/user_level_stat.csv") as f:
    reader = csv.reader(f)
    for row in reader:
        labelkeys.append(row[0])
        datas.append(int(row[1]))
    
fig = px.bar(pd.DataFrame(datas,index=labelkeys))
fig.update_xaxes(title="レベル")
fig.update_yaxes(title="人数")
fig.update_layout(title="ユーザレベル帯ごとの人数")
fig.show()

