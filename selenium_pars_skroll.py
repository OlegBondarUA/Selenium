from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('headless')
chrome_options.add_argument("disable-gpu")
driver = webdriver.Chrome(executable_path='./chromedriver',
                          chrome_options=chrome_options
                          )
driver.maximize_window()
driver.get('https://ua.factcool.com/category/1601')

pagination = driver.find_elements(By.CSS_SELECTOR, 'div.sc-b06d436d-0.sc-3a7f9fdd-0.jsdYSC')
for page in pagination:
    driver.implicitly_wait(10)
    container = driver.find_element(By.CSS_SELECTOR, 'div.sc-6172c6be-2.jQPAhG')
    driver.execute_script("arguments[0].scrollIntoView(true);", container)
# actions = ActionChains(driver)
# actions.move_to_element(element).perform()