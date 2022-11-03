from seleniumwire import webdriver
import time
import random
from fake_useragent import UserAgent


user_agent_list = [
    'python',
    'the best',
    'hi my friend'
]
# proxy_options = {
#     'proxy': {
#         'https': f'https://{login}:{password}@138.128.91.65:8077'
#     }
# }
useragent = UserAgent(verify_ssl=False)

# options
chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument(f'user-agent={random.choice(user_agent_list)}')
# chrome_options.add_argument(f'user-agent={useragent.random}')
chrome_options.add_argument('--proxy-server=138.128.91.65:8077')

driver = webdriver.Chrome(executable_path='./chromedriver',
                          chrome_options=chrome_options
                          )
try:

    # driver.get(url='https://www.whatismybrowser.com/detect/what-is-my-user-agent')
    driver.get('https://www.ipaddress.my')
    time.sleep(10)

except Exception as error:
    print(error)

finally:
    driver.close()
    driver.quit()
