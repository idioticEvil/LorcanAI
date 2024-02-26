from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from lxml import etree
import time
import cardClasses

options = Options()
#options.add_argument('--headless')
options.page_load_strategy = 'eager'
driver = webdriver.Firefox(options=options)
driver.get('https://lorcanaplayer.com/lorcana-card-list/#main-sets')
soup = None
dom = None
charCards = []
locCards = []
actCards = []
songCards = []
itemCards = []

cardLinkTDs = driver.find_elements(By.CSS_SELECTOR, 'td.card-name')

def getCardInfo():
    name = soup.find("p", class_="gb-headline gb-headline-61acf78d gb-headline-text").text
    
    print(name)

for td in cardLinkTDs:
    link = td.find_element(By.TAG_NAME, 'a')
    linkHREF = link.get_attribute('href')
    print("Opening: " + linkHREF)

    driver.execute_script(f"window.open('{linkHREF}', '_blank')")
    driver.switch_to.window(driver.window_handles[1])
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'p.gb-headline.gb-headline-61acf78d.gb-headline-text')))

    soup = BeautifulSoup(driver.page_source, 'lxml')
    dom = etree.HTML(str(soup))

    getCardInfo()

    driver.close()
    driver.switch_to.window(driver.window_handles[0])

