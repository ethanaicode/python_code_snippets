from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.chrome.options import Options

import time

def main():
    chrome_options = Options()
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option('useAutomationExtension', False)

    # Create a new instance of the Chrome driver
    driver = webdriver.Chrome(options=chrome_options)

    # go to the google home page
    driver.get("http://www.google.com")

    # find the element that's name attribute is q (the google search box)
    inputElement = driver.find_element(By.NAME, "q")

    # type in the search
    inputElement.send_keys("cheese!")

    # submit the form (although google automatically searches now without submitting)
    inputElement.submit()

    try:
        # we have to wait for the page to refresh, the last thing that seems to be updated is the title
        WebDriverWait(driver, 10).until(EC.title_contains("cheese!"))

        # You should see "cheese! - Google Search"
        print(driver.title)

    finally:
        time.sleep(10000)
        driver.quit()

if __name__ == "__main__":
    main()


