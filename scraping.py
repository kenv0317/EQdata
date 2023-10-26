from bs4 import BeautifulSoup
import requests
import json
# import requests_cache                              

# 設定とHTML取得，構文解析
HEADERS = {'User-Agent': 'Mozilla/5.0'}              
response = requests.get('https://ja.wikipedia.org/wiki/%E5%9C%B0%E9%9C%87%E3%81%AE%E5%B9%B4%E8%A1%A8', headers=HEADERS)  # HTML取得
soup = BeautifulSoup(response.content, "lxml")

# 目当てのtable要素を取得
#main = soup.select_one('.mw-parser-output')

def make_data2():
    data = []
    d = dict(location="発生地域",year="9999",name="地震名")
    data.append(d)
    location_list = location()
    location_num = -1
    year = ''
    name = ''
    count = 0
    for li in soup.select('ul')[2:]:
        text = li.text
        text = text.split()
        text_year = [s for s in text if ('年' and '月' and '日') in s]
        idx = 0
        for i in range(len(text_year)):
            target = '。'
            if target in text_year[i]:
                idx = text_year[i].find(target)  # 半角空白文字のインデックスを検索
                text_year[i] = 'del'
        if 'del' in text_year: text_year.remove('del')
        text_name = [s for s in text if '地震' in s]
        #text_M = [s for s in text if 'M' in s]
        if len(text_year) != 0:
            if len(text_year) == len(text_name):
                for i in range(len(text_year)):
                    year = text_year[i]
                    target = '年'
                    if target in year:
                        idx = year.find(target)  # 半角空白文字のインデックスを検索
                        year = year[:idx]  # スライスで半角空白文字のインデックスまでを抽出
                    target = '、'
                    if target in year:
                        idx = year.find(target)  # 半角空白文字のインデックスを検索
                        year = year[idx+1:]  # スライスで半角空白文字のインデックス後を抽出
                    name = text_name[i]
                    #M = text_M[i]
                    try:
                        if year != '' and name != '':
                            if int(year) < int(data[-1]['year']): #前の年よりも小さいならlocation変更
                                location_num += 1
                            d = dict(location=location_list[location_num],year=int(year),name=name)
                            data.append(d)
                    except ValueError:
                        pass
    return data[1:]