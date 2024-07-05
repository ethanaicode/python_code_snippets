from seleniumwire import webdriver
import requests
import time
import json

# 获取代理ip
def get_ip_list():
    # ip_dict_list = [
    #     {
    #         "ip": "49.76.47.235",
    #         "port": "40034"
    #     }
    # ]
    # return ip_dict_list

    # 获取是用到的密钥，用来对应套餐
    secrect = 'bzqlgt4e'
    url = f"http://api.tianqiip.com/getip?secret={secrect}&num=1&type=json&port=1&time=3&mr=1&sign=49b327cc021a444262d48cf2012b6574"
    resp = requests.get(url)
    # 提取页面数据
    resp_json_dict = json.loads(resp.text)
    ip_dict_list = resp_json_dict.get('data')
    return ip_dict_list

# 通过代理访问网站
def main(ip_port, url):
    proxy_options = {
        'proxy': {
            'http': 'http://' + ip_port,
            'https': 'https://' + ip_port,
            # 'http': 'socks5://127.0.0.1:9999',
            # 'https': 'socks5://127.0.0.1:9999',
            'no_proxy': 'localhost,127.0.0.1'  # Bypass proxy for local addresses
        }
    }

    # Initialize the Chrome driver with the specified proxy options
    driver = webdriver.Chrome(seleniumwire_options=proxy_options)

    # Define a request interceptor to add custom headers
    def interceptor(request):
        request.headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    driver.request_interceptor = interceptor

    # Use the driver as usual
    driver.get(url)

    time.sleep(60)

    # Close the browser when process is done
    driver.quit()

if __name__ == '__main__':

    # 要访问的网站
    url = 'https://ipv4.geojs.io/'
    # url = 'https://ip138.com/'
    # url = 'https://rtest.itemvs.com/test/test'

    # 获取代理ip列表
    ip_dict_list = get_ip_list()

    # 先只取第一个ip
    ip_dict = ip_dict_list[0]
    ip_port = f'{ip_dict.get("ip")}:{ip_dict.get("port")}'
    # ip_port = ''

    # 用这个IP进行代理访问
    main(ip_port, url)
 