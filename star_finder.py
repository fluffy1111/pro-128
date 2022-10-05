from math import radians
from msilib import Table
from turtle import distance
from bs4 import BeautifulSoup
import pandas as pd
from selenium.webdriver.common.by import By
import time
from selenium import webdriver

bright_stars = 'https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars'
browser = webdriver.Chrome('C:/Users/maxwe/Downloads/pro 127/chromedriver.exe')
browser.get(bright_stars)
time.sleep(10)

scraped_data = []
def scrape():
    soup = BeautifulSoup(browser.page_source, 'html.parser')
    wiki = soup.find('table', attrs = {"class", "wikitable"})
    table_body = wiki.find('tbody')
    table_rows = table_body.find_all('tr')

    for row in table_rows:
        table_cols = row.find_all('td')
        print(table_cols)
        temp_list = []

        for col_data in table_cols:
            print(col_data.text)
            data = col_data.text.strip()
            print(data)
            temp_list.append(data)

        scraped_data.append(temp_list)
scrape()

stars_data = []
for i in range(0,len(scraped_data)):

    star_names = scraped_data[i][1]
    Distance = scraped_data[i][3]
    mass = scraped_data[i][5]
    radius = scraped_data[i][6]
    lum = scraped_data[i][7]

    required_data = [star_names, Distance, mass, radius, lum]
    stars_data.append(required_data)

headers = ['star_name','distance','mass','radius','liminosity']
star_df_1 = pd.DataFrame(stars_data, columns = headers)

star_df_1.to_csv('scraped_data.csv',index=True, index_label="id")