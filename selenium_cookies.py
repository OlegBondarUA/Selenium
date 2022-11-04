import time
import pickle

from seleniumwire import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from decouple import config


login = config('LOGIN_FACEBOOK')
password = config('PASSWORD_FACEBOOK')

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(
    f'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
    f'(KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.59'
)

driver = webdriver.Chrome(executable_path='./chromedriver',
                          chrome_options=chrome_options
                          )

try:

    driver.get(url='https://www.facebook.com')
    time.sleep(5)

    # email_input = driver.find_element(By.CSS_SELECTOR, 'input[id="email"]')
    # email_input.clear()
    # email_input.send_keys(login)
    # time.sleep(5)
    #
    # password_input = driver.find_element(By.CSS_SELECTOR, 'input[id="pass"]')
    # password_input.clear()
    # password_input.send_keys(password)
    # time.sleep(5)
    # password_input.send_keys(Keys.ENTER)
    #
    # # login_button = driver.find_element(By.CSS_SELECTOR, '[type="submit"]')
    # # login_button.click()
    #
    # pickle.dump(driver.get_cookies(), open(f'{login}_cookies', 'wb'))

    for cookie in pickle.load(open(f'{login}_cookies', 'rb')):
        driver.add_cookie(cookie)

    time.sleep(3)
    driver.refresh()
    time.sleep(15)


except Exception as error:
    print(error)

finally:
    driver.close()
    driver.quit()
