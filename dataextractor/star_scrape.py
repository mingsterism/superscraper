from bs4 import BeautifulSoup
import requests 
import lxml
#import pandas as pd

def scrape_star(base_url):

    #base_url = "https://www.thestar.com.my/business/"

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}

    star_page = requests.get(base_url, headers=headers)

    if star_page.status_code == requests.codes.ok:
        soup = BeautifulSoup(star_page.content, "lxml")

    titles_row = soup.find_all("div", class_="in-sec-story")

    title_list = []

    for title in titles_row:

        right_title = title.h2.a.text 
        #print(soup)
        print(right_title)
        title_list.append(right_title)

    #print(title_list)

    return title_list






