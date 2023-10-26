# EQdata

世界の主な地震のデータを可視化するサイトです。  
棒グラフと円グラフの2種類あり、どちらも発生地域と発生件数を用いてグラフ化しています。
表に関しては、発生地域、発生年、地震の名前が一覧になっています。
ページ上部のボタンを押すとグラフに関しては、そのボタンに書かれた地域が赤色にハイライトされ、
表に関してはそのボタンに書かれた地域のみに絞れれたデータの一覧が表示されるようになります。  

![EQdata_out](https://github.com/kenv0317/EQdata/assets/71165696/3b37a4db-5b00-4585-9235-53eb6bbdc19d)

## 各スクリプトについて
- Templates
  - index.html  (HTML, CSS, JavaScriptを記述したファイル)
- project.py  (Webアプリ本体(Flaskアプリ))
- scraping.py  (スクレイピング用ファイル)
- main-earthquake.json  (スクレイピングしたデータのjsonファイル)
- api
  - server_eve.py  (データAPI(Eve+Flask))
  - setting.py  (データAPIの設定ファイル)
 

## データの収集について
地震の年表(https://ja.wikipedia.org/wiki/%E5%9C%B0%E9%9C%87%E3%81%AE%E5%B9%B4%E8%A1%A8) からスクレイピングで取得

## 使用技術
- Python
- Beautiful Soup
- Flask
- Eve
- MongoDB
- JavaScript
- D3.js
