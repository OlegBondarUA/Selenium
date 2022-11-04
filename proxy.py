import time

from seleniumwire import webdriver
from decouple import config


login = config('LOGIN_PROXY')
password = config('PASSWORD_PROXY')


proxy_options = {
    'proxy': {
        'https': f'https://{login}:{password}@138.128.91.65:8077'
    }
}

# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--proxy-server=138.128.91.65:8077')

driver = webdriver.Chrome(executable_path='./chromedriver',
                          seleniumwire_options=proxy_options
                          )

try:

    driver.get('https://www.ipaddress.my')
    time.sleep(10)

except Exception as error:
    print(error)

finally:
    driver.close()
    driver.quit()
