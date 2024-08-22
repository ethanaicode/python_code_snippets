import requests

# URL of the request
url = "https://source.showdoc.com.cn/server/index.php?s=/api/page/info"

# Headers
headers = {
    # "Accept": "application/json, text/plain, */*",
    # "Accept-Encoding": "gzip, deflate, br, zstd",
    # "Accept-Language": "en,zh-CN;q=0.9,zh-TW;q=0.8,zh;q=0.7",
    # "Content-Type": "application/x-www-form-urlencoded",
    # "Dnt": "1",
    "Origin": "https://www.showdoc.com.cn",
    "Referer": "https://www.showdoc.com.cn/",
    # "Sec-Ch-Ua": '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    # "Sec-Ch-Ua-Mobile": "?0",
    # "Sec-Ch-Ua-Platform": '"macOS"',
    # "Sec-Fetch-Dest": "empty",
    # "Sec-Fetch-Mode": "cors",
    # "Sec-Fetch-Site": "same-site",
    # "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
}

# Cookies
cookies = {
    # "think_language": "en",
    "PHPSESSID": "9c3970187535c086c2d1c7efff137413"
}

# Data to be sent in the POST request
data = {
    'page_id': '11153045971162270',
    # '_item_pwd': 'Sucang'
}

# Send the POST request
response = requests.post(url, headers=headers, cookies=cookies, data=data)

# Print the response
print(response.text)
