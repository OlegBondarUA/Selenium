import time
import random

from selenium import webdriver
from fake_useragent import UserAgent


user_agent_list = [
    'python',
    'the best',
    'hi my friend'
]

useragent = UserAgent(verify_ssl=False)

# options
chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument(f'user-agent={random.choice(user_agent_list)}')
chrome_options.add_argument(f'user-agent={useragent.random}')

driver = webdriver.Chrome(executable_path='./chromedriver',
                          chrome_options=chrome_options
                          )
try:

    driver.get(url='https://www.whatismybrowser.com/detect/what-is-my-user-agent')
    time.sleep(10)

except Exception as error:
    print(error)

finally:
    driver.close()
    driver.quit()
