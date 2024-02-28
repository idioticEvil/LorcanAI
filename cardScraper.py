from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from lxml import etree
import cardClasses

# Note: All card data will be scraped from https://lorcanaplayer.com/lorcana-card-list/#main-sets
# Make sure to exclude all cards with enchanted or promo rarity for final pass

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

def extractLinkText(soup, targetClass, subClass):
    subSoup = soup.find('div', class_=targetClass)
    all_links = subSoup.find('p', class_=subClass).find_all('a')
    strings = [link.text.strip() for link in all_links]
    return strings[0] if len(strings) == 1 else strings

def getCardInfo():
    name = soup.find("p", class_="gb-headline gb-headline-61acf78d gb-headline-text").text
    imageURL = soup.find("img", class_="gb-image-b699f858 skip-lazy card")['src']
    inkableText = extractLinkText(soup, 'gb-container gb-container-660cda70', 'has-text-align-center')
    expansionText = extractLinkText(soup, 'gb-container gb-container-7423ff29', 'has-text-align-center')
    inkColorText = extractLinkText(soup, 'gb-container gb-container-6c8450e1', 'has-text-align-center')
    cardTypeText = extractLinkText(soup, 'gb-container gb-container-686ee32f', 'has-text-align-center')
    rarityText = extractLinkText(soup, 'gb-container gb-container-27860a78', 'has-text-align-center')
    classificationsText = extractLinkText(soup, 'gb-container gb-container-0b93f10d', 'gb-headline gb-headline-fea62c4a gb-headline-text')
    inkCostText = soup.find('p', class_="gb-headline gb-headline-55c56612 gb-headline-text").text
    print("Card Name: " + name)
    print("Image URL: " + imageURL)
    print("Inkable: " + inkableText)
    print("Expansion: " + expansionText)
    print("Ink Color: " + inkColorText)
    print("Card Type: " + cardTypeText)
    print("Rarity: " + rarityText)
    print("Ink Cost: " + inkCostText)
    
    if isinstance(classificationsText, list):
        for classification in classificationsText:
            print("Classification: " + classification)
    else:
        print("Classification: " + classificationsText)

    inkable = inkableText == "Yes"
    expansion = cardClasses.Expansion[expansionText]
    inkColor = cardClasses.CardInkColor[inkColorText]
    cardType = cardClasses.CardType[cardTypeText]
    rarity = cardClasses.CardRarity[rarityText]
    classifications = [cardClasses.CardClassification[classification] for classification in classificationsText]
    inkCost = int(inkCostText)


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
