import time

from seleniumwire import webdriver
from selenium.webdriver.common.by import By


# options
chrome_options = webdriver.ChromeOptions()
# option background mode
chrome_options.add_argument('headless')
# options user-agent
chrome_options.add_argument(
    f'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
    f'(KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.59'
)
# option disable-blink-webdriver
chrome_options.add_argument('--disable-blink-features=AutomationControlled')

driver = webdriver.Chrome(executable_path='./chromedriver',
                          chrome_options=chrome_options
                          )

try:

    driver.get(url='https://www.youtube.com/')
    print('open url')
    time.sleep(3)

    email_input = driver.find_element(By.CSS_SELECTOR, '[id="avatar-link"]')
    email_input.click()
    print('start video')

    time.sleep(20)

except Exception as error:
    print(error)

finally:
    driver.close()
    driver.quit()
