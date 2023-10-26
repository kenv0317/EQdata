# coding: utf-8

MONGO_URI = 'mongodb://localhost/earthquake_data'  # 接続先MongoDBのドメイン:ポート番号(ここでは50001)
X_DOMAINS = '*'               # このAPIへのアクセス許可ドメイン
HATEOAS = False               # Restfulの拡張
PAGINATION = False            # ページ送り
URL_PREFIX = 'api'            # このAPIのURL接頭辞 http://localhost:50001/api 
DOMAIN = {'main-earthquake':{    # 公開するmongodbコレクション名
    'item_title': 'earthquakes',  # 返されるjsonファイルにおけるkey
    'url':'earthquakes',          # 公開用のurl http://localhost:50001/api/winners
    'schema':{
        'location':{'type':'string'},  # 以降，jsonファイルに含めるmongodbのフィールド(キー)名と型
        'year':{'type':'integer'},
        'name':{'type':'string'}, 
        }
}}
