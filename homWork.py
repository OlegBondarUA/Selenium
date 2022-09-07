from selenium import webdriver
from selenium.webdriver.common.by import By
import json


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('headless')
chrome_options.add_argument('window-size=1920x1080')
chrome_options.add_argument("disable-gpu")
driver = webdriver.Chrome(executable_path='./chromedriver',
                          chrome_options=chrome_options)
driver.implicitly_wait(5)
driver.get("https://www.google.com.ua/?hl=uk")


def setSearchReq(str):
    googleInput = driver.find_element(By.CSS_SELECTOR, 'input[name="q"]')
    googleInput.send_keys(str)
    submit = driver.find_element(By.CSS_SELECTOR, '[type="submit"]')
    submit.click()


def getSerchResults(str):
    setSearchReq(str)
    els = driver.find_elements(By.CSS_SELECTOR, '.g[lang]')
    data = {}
    # print(els)
    for i, e in enumerate(els):
        # print(e)
        data[i+1] = {
            'link': e.find_element(By.CSS_SELECTOR, 'a').get_attribute('href'),
            'title': e.find_element(By.CSS_SELECTOR, 'h3').text
        }

    with open('searchResult.json', 'w') as file:
        json.dump(data, file, indent=4)

    driver.quit()


getSerchResults('Python programming')
