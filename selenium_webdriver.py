import time

from seleniumwire import webdriver


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(
    f'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
    f'(KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.59'
)
chrome_options.add_argument('--disable-blink-features=AutomationControlled')

driver = webdriver.Chrome(executable_path='./chromedriver',
                          chrome_options=chrome_options
                          )

try:
    driver.get('https://intoli.com/blog/not-possible-to-block-chrome-headless/chrome-headless-test.html')
    time.sleep(10)

except Exception as error:
    print(error)

finally:
    driver.close()
    driver.quit()
