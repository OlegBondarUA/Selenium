import time
import random
from seleniumwire import webdriver
from selenium.webdriver.common.by import By
from multiprocessing import Pool


# options
chrome_options = webdriver.ChromeOptions()
# option disable-blink-webdriver
chrome_options.add_argument('--disable-blink-features=AutomationControlled')
driver = webdriver.Chrome(executable_path='./chromedriver',
                          chrome_options=chrome_options
                          )


def get_data(url):
    try:
        driver.get(url=url)
        time.sleep(5)
        driver.find_element(By.CSS_SELECTOR,
                            'div.tiktok-kd7foj-DivVideoWrapper.e1bh0wg716'
                            ).find_element(By.CSS_SELECTOR,
                                           'div[data-e2e="feed-video"]').click()
        time.sleep(random.randrange(3, 10))
    except Exception as error:
        print(error)

    finally:
        driver.close()
        driver.quit()


if __name__ == '__main__':
    process_count = int(input('Enter the number of processes: '))
    url_ = input('Enter the URL: ')
    urls_list = [url_] * process_count
    pool = Pool(processes=process_count)
    pool.map(get_data, urls_list)
