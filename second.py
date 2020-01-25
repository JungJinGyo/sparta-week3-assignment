import requests
from bs4 import BeautifulSoup
from selenium import webdriver

if __name__ == '__main__':
    options = webdriver.ChromeOptions()
    # options.add_argument('headless')
    options.add_argument('windows-size=1920x1080')
    options.add_argument('disable-gpu')
    driver = webdriver.Chrome('C:/Users/gkom5/OneDrive/Desktop/sparta/Week3-PY/chromedriver.exe', options=options)
    driver.get('https://select.ridibooks.com/book/510000165')

    print(driver.page_source)
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    # soup.....