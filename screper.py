import requests
from concurrent.futures import ThreadPoolExecutor
from queue import Queue
from selenium import webdriver
from selenium.webdriver.common.by import By


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('headless')
chrome_options.add_argument("disable-gpu")
driver = webdriver.Chrome(executable_path='./chromedriver',
                          chrome_options=chrome_options
                          )
driver.maximize_window()

TIME_OUT = 10


def get_url(url: str):
    links = []

    driver.get(url)
    driver.implicitly_wait(5)
    item = driver.find_elements(By.CSS_SELECTOR, 'div[class="ProductCard__main"]')
    for number, element in enumerate(item):
        url_ = element.find_element(By.CSS_SELECTOR, 'a').get_attribute('href')
        links.append(url_)

    with open('links.txt', 'a') as file:
        for line in links:
            file.write(line + '\n')


def worker(queue: Queue):
    while True:
        url = queue.get()
        print('[WORKING ON]', url)
        try:
            with requests.Session() as session:
                response = session.get(
                    url,
                    allow_redirects=True,
                    timeout=TIME_OUT
                )
                print(response.status_code)

                if response.status_code == 404:
                    print('Page not found', url)
                    break

                assert response.status_code in (200, 301, 302), 'Bad response'

            get_url(url)

        except (
                requests.Timeout,
                requests.TooManyRedirects,
                requests.ConnectionError,
                requests.RequestException,
                requests.ConnectTimeout,
                AssertionError
        ) as error:
            print('An error happen', error)
            queue.put(url)

        if queue.qsize() == 0:
            break


def main():
    queue = Queue()
    url = 'https://kvshop.com.ua/smartfony/apple/'
    pages = 2

    for page in range(1, pages + 1):
        queue.put(url + str(page))

    worker_number = 2

    with ThreadPoolExecutor(max_workers=worker_number) as executor:
        for _ in range(worker_number):
            executor.submit(worker, queue)

    driver.quit()


if __name__ == '__main__':
    main()
