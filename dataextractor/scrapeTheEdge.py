import requests
from bs4 import BeautifulSoup
import lxml.html
import webbrowser
import pandas as pd


def data_extractor():
    # Edge
    titles = ["Title", "Date", "Contents"]
    df1 = pd.DataFrame(columns=titles)

    i = 1
    for page_name in ["", "?page=1"]:
        url = 'http://www.theedgemarkets.com/search-results' + page_name

        page = requests.get(url)
        html = page.content
        soup = BeautifulSoup(html, "lxml")
        containers = soup.findAll("div", {"class": "views-row"})

        for container in containers:
            title_container = container.find("div", {"class": "views-field views-field-title"})

            # article name
            article_name = title_container.span.a.text

            # article link
            news_link = "http://www.theedgemarkets.com" + title_container.span.a['href']
            sub_page = requests.get(news_link)
            sub_html = sub_page.content
            sub_soup = BeautifulSoup(sub_html, "lxml")

            # article date
            article_date = sub_soup.find("span", {"class": "post-created"}).text

            # article content
            article_text = ''
            article = sub_soup.findAll("div", {"property": "content:encoded"})
            for p in article:
                article_text += ''.join(p.findAll(text=True))

            df1.loc[i] = [article_name, article_date, article_text]
            i = i + 1

    i + 1

    # df1.to_json(r'theEdge.json')
    data = df1.to_json()
    return data

# data_extractor()
