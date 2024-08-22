import requests

# Define User-Agents for different devices
user_agents = {
    # 'windows desktop': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'mac desktop': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
    # 'mobile': 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1',
    # 'wechat': 'WeChat/28486 CFNetwork/1410.4 Darwin/22.6.0',
}

# Function to make a request with a specified User-Agent
def fetch_url(url, headers):
    response = requests.get(url, headers=headers)
    return response.text

# URL to request
# url = "https://sh.58.com/"
url = "https://rtest.itemvs.com/test/test"

# Fetch and print content as seen by different devices
for device in user_agents:
    print(f"\nFetching content as {device} device...")
    headers = {'User-Agent': user_agents[device]}
    # add more header
    headers['Referer'] = 'https://www.baidu.com'
    content = fetch_url(url=url, headers=headers)
    # print(content[:500])  # Print the first 500 characters of the response
    print(content)
