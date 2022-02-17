# -*- coding: utf-8 -*-
#!/usr/bin/env python

import codecs,re,time,datetime
from msilib.schema import File

# #テキストファイルをインポート(読み込む)
txt = codecs.open('TypeHereYour.txt','r',encoding='utf-8')

# #テキストファイルを一行ずつ読み込む。
tx_list = txt.readlines()

#ユニークファイル名にするために時間をファイル名にする
date = datetime.datetime.now()
DF = date.strftime('%Y-%m-%d-%H-%M-%S')

#新規テキストファイルを作成する。(---.txt)
FileName = 'made/' + DF + '.txt'
oF = codecs.open(FileName,'w',encoding='utf-8')

#置換開始
for tx_line in tx_list:
    
    #置き換え完了した文字リストを新規テキストファイルに書き込む。
    Fi = tx_line.replace('(','《')
    Se= Fi.replace(')','》')
    oF.writelines(Se)
    
    # print(Se)

oF.close()