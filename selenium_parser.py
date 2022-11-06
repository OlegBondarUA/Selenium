from selenium import webdriver
from selenium.webdriver.common.by import By
import json

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('window-size=1920x1080')
chrome_options.add_argument("disable-gpu")
driver = webdriver.Chrome(executable_path='./chromedriver',
                          chrome_options=chrome_options
                          )
driver.implicitly_wait(5)
driver.get('https://prom.ua/ua/Umnye-chasy-i-braslety')


def get_url_watch():
    item = driver.find_elements(By.CSS_SELECTOR,
                                'div[class="l-GwW js-productad"]')
    data = {}

    for number, element in enumerate(item):

        data[number + 1] = {
            'url': element.find_element(By.CSS_SELECTOR, 'a').get_attribute('href'),
            'title': element.find_element(By.CSS_SELECTOR, 'span').text.strip(),
            'price': element.find_element(By.CSS_SELECTOR, 'div[class="M3v0L Qa-Dw _0-YBE mpcTk _0Jq1n"] span').text.strip().replace('\xa0', '')
        }
    with open('catalog_watch.json', 'w') as file:
        json.dump(data, file, indent=4,
                  ensure_ascii=False,
                  separators=(',', ': '))

    driver.quit()


get_url_watch()
