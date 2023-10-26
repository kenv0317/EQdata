# coding: utf-8

from eve import Eve

app = Eve()

if __name__=='__main__':
    app.run(host='127.0.0.1', port=50008, debug=True)   # データAPI(Eve)のポート番号．各自変更
