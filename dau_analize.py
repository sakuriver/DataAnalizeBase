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
with open("./sample/dau.csv") as f:
    reader = csv.reader(f)
    for row in reader:
        labelkeys.append("2023/{}".format(row[0]))
        datas.append(int(row[1]))
    
fig = px.line(pd.DataFrame(datas,index=labelkeys))
fig.update_xaxes(title="date")
fig.update_yaxes(title="dau")
fig.update_layout(title="全体のDAU")
fig.show()

