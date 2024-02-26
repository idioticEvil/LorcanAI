from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from lxml import etree
import requests
import time
import cardClasses

options = Options()
options.add_argument('--headless')
options.page_load_strategy = 'eager'
driver = webdriver.Firefox(options=options)
driver.get('https://lorcanaplayer.com/lorcana-card-list/#main-sets')

cardLinkTDs = driver.find_elements(By.CSS_SELECTOR, 'td.card-name')

for td in cardLinkTDs:
    link = td.find_element(By.TAG_NAME, 'a')
    linkHREF = link.get_attribute('href')
    print("Opening: " + linkHREF)

    driver.execute_script(f"window.open('{linkHREF}', '_blank')")
    driver.switch_to.window(driver.window_handles[1])

    time.sleep(1)

    driver.close()
    driver.switch_to.window(driver.window_handles[0])

