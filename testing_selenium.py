from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time
import matplotlib.pyplot as plt
def amazon(products):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get("https://www.amazon.com")
    time.sleep(2)
    search_box = driver.find_element(By.XPATH, "//input[@id='twotabsearchtextbox']")
    search_box.send_keys(products)
    search_box.send_keys(Keys.RETURN)
    time.sleep(2)
    try:
        rating_filter = driver.find_element(By.XPATH, "//span[contains(text(),'4 Stars')]")
        rating_filter.click()
        time.sleep(3)
    except:
        print("not found")
    titles = []
    prices = []
    # ratings = []
    links = []
    items = driver.find_elements(By.XPATH, "//div[@data-component-type='s-search-result']")
    for item in items[:30]:
        try:
            title = item.find_element(By.TAG_NAME, "h2").text
            titles.append(title)
        except:
            titles.append("no title found")
        try:
            price = item.find_element(By.CSS_SELECTOR, "span.a-price-whole").text
            prices.append(price)
        except:
            prices.append("no price ")
        try:
            link = item.find_element(By.TAG_NAME, "a").get_attribute("href")
            links.append(link)
        except:
            links.append("not found")
    driver.quit()
    data = {
        "Product Name": titles,
        "Price": prices,

        "Product Link": links
    }
    df = pd.DataFrame(data)
    df.to_csv("amazon_products.csv", index=False)
    print("Data saved to amazon_products.csv")
    print(df)
user_search = input("Enter the product you want to search on Amazon: ")
amazon(user_search)









