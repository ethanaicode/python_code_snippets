from browsermobproxy import Server
from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import requests
import sys

# Start the BrowserMob Proxy server
server = Server("/Users/ethan/Downloads/Dev_Set/driver/browsermob-proxy-2.1.4/bin/browsermob-proxy")
server.start()
proxy = server.create_proxy()

# Set up proxy settings for Selenium
proxy.selenium_proxy()

# Set up the proxy for the Chrome browser
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(f"--proxy-server={proxy.proxy}")

# Directly use the ChromeDriver in the PATH
driver = webdriver.Chrome(chrome_options=chrome_options)

# Set custom headers
proxy.new_har("example.com", options={'captureHeaders': True})
proxy.headers({"Referer": "https://www.baidu.com"})

# Open the website
# driver.get("https://www.autohome.com.cn/")
driver.get("https://rtest.itemvs.com/test/test")

# Verify the request headers
for entry in proxy.har['log']['entries']:
    request_headers = entry['request']['headers']
    print(request_headers)

concent = driver.page_source
print("\nThe content of the page is: ", concent)

# close the browser
driver.quit()

# stop the BrowserMob Proxy server
server.stop()