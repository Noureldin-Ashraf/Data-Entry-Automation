import requests
from bs4 import BeautifulSoup
from selenium import webdriver


# Zillow URL which contains the rental real estate data
zillow_url = 'https://www.zillow.com/san-francisco-ca/rentals/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3A%22San%20Francisco%2C%20CA%22%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56825534228516%2C%22east%22%3A-122.29840365771484%2C%22south%22%3A37.69668892292081%2C%22north%22%3A37.85381150365383%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A20330%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22min%22%3A0%2C%22max%22%3A872627%7D%2C%22mp%22%3A%7B%22min%22%3A0%2C%22max%22%3A3000%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D'

# Some websites requires a user agent and language to show the appropriate webpage, so we need to send them in the request header
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
accept_language = "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"

headers = {
    "User-Agent": user_agent,
    "Accept-Language": accept_language,
}

response = requests.get(zillow_url, headers=headers)
zillow_webpage = response.text
soup = BeautifulSoup(zillow_webpage, "html.parser")

# Create empty lists for (Addresses, Prices and URLs) 
address_list = []
price_list = []
link_list = []

articles = soup.select('article')
for article in articles:
    # Get (Addresses, Prices and URLs) data and populate the lists with it
    address_list.append(article.find("address", attrs={'data-test': 'property-card-addr'}).text)
    price_list.append(article.find("span", attrs={'data-test': 'property-card-price'}).text)
    link = article.select_one('a').get("href")
    if "https" not in link:
        # Add the URL prefix in case it doesn't exist.
        link = "https://www.zillow.com" + link
    link_list.append(link)


# Create a Selenium webdriver to interact with the google form
chrome_driver_path = "C:/chrome_driver/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

# Start looping on the lists and populate the form elements per list element
for i in range(len(address_list)):
    # Google Form URL
    google_form_url='https://docs.google.com/forms/d/e/1FAIpQLSek__J_P2wufcIoWmD9uf8MYYwGbBAjP2yebM7M5vE1CS1sbA/viewform?usp=sf_link'
    driver.get(google_form_url)

    # Instruct the webdriver to aquire each element and the button
    address_box = driver.find_element("xpath",
                                      '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price_box = driver.find_element("xpath",
                                    '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link_box = driver.find_element("xpath",
                                   '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    submit_btn = driver.find_element("xpath",
                                     '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')

    # Hold the actions for 3 seconds for testing purposes 
    #time.sleep(3)

    # Populate the form elements with the data and click the button
    address_box.send_keys(address_list[i])
    price_box.send_keys(price_list[i])
    link_box.send_keys(link_list[i])
    submit_btn.click()


