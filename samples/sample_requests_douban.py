import requests

# 指定爬取地址
url = 'https://movie.douban.com/j/chart/top_list'
params = {
    'type': '5',
    'interval_id': '100:90',
    'action': '',
    'start': '0',
    'limit': '20'
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}

# 发起get请求返回值为响应对象
response = requests.get(url=url, params=params, headers=headers)

# 获取相应数据
response.encoding = 'utf-8'
page_text = response.json() # json数据格式化
# 解析出电影的名称+评分
for each in page_text:
    title = each['title']
    score = each['score']
    print(title, score)