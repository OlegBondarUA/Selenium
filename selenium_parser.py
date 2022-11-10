from selenium import webdriver
from selenium.webdriver.common.by import By
import json

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('window-size=1920x1080')
chrome_options.add_argument("disable-gpu")
driver = webdriver.Chrome(executable_path='./chromedriver',
                          chrome_options=chrome_options
                          )


def get_url_watch():
    list_ = []

    for page in range(1, 3, 1):

        url = 'https://prom.ua/ua/Umnye-chasy-i-braslety;' + str(page)
        driver.get(url)
        driver.implicitly_wait(5)
        item = driver.find_elements(By.CSS_SELECTOR, 'div[data-product-id]')

        for i, element in enumerate(item):

            url = element.find_element(By.CSS_SELECTOR, 'a').get_attribute('href')

            list_.append({
                'url': url,
                'title': element.find_element(By.CSS_SELECTOR, 'a').get_attribute('title'),
                # 'old_price': element.find_element(By.CSS_SELECTOR, 'span[data-qaid="old_price"]').get_attribute('data-qaprice'),
                'price': element.find_element(By.CSS_SELECTOR, 'span[data-qaid="product_price"]').get_attribute('data-qaprice')
            })

    driver.quit()

    with open('catalog_watch.json', 'w') as file:
        json.dump(list_, file, indent=4,
                  ensure_ascii=False,
                  separators=(',', ': '))


def main():

    get_url_watch()


if __name__ == '__main__':
    main()