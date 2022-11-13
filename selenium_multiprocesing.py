import time
from seleniumwire import webdriver
from multiprocessing import Pool


# options
chrome_options = webdriver.ChromeOptions()
# option disable-blink-webdriver
chrome_options.add_argument('--disable-blink-features=AutomationControlled')

urls_list = ['https://stackoverflow.com',
             'https://www.youtube.com',
             'https://www.facebook.com'
             ]


def get_data(url):
    try:
        driver = webdriver.Chrome(executable_path='./chromedriver',
                                  chrome_options=chrome_options
                                  )
        driver.get(url=url)
        time.sleep(5)
        driver.get_screenshot_as_file(f'media/{url.split("//")[1]}.png')
    except Exception as error:
        print(error)

    finally:
        driver.close()
        driver.quit()


if __name__ == '__main__':
    pool = Pool(processes=3)
    pool.map(get_data, urls_list)
