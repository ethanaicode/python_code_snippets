from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import requests
import sys

# Directly use the ChromeDriver in the PATH
driver = webdriver.Chrome()

# Open the website
# driver.get("https://www.autohome.com.cn/")
# driver.get("https://rtest.itemvs.com/test/test")
driver.get("https://kimi.moonshot.cn/")

time.sleep(60)
sys.exit()

# get the title of the page
print("\nThe title of the page is: ", driver.title)

# wait for 0.5 second
driver.implicitly_wait(0.5)

# input the search query
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("BMW")

# submit the search query
search_box.send_keys(Keys.RETURN)

# wait for 5 second
time.sleep(5)

# click on the first search result
search_result = driver.find_element(By.LINK_TEXT, "宝马3系")
search_result.click()

# wait for 3 second
time.sleep(5)

content = driver.page_source
print("\nThe content of the page is: ", content)

# find the element by class name


# # find class name
# element = driver.find_element(By.CLASS_NAME, "pic-main")

# # find img tag
# element = element.find_element(By.TAG_NAME, "img")

# # Extract the image URL from the 'src' attribute
# img_url = element.get_attribute("src")
# print("\nThe image URL is: ", img_url)

# # wait for 3 second
# time.sleep(3)

# # close the browser
driver.quit()