# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup

def fetchUrlList(kanban, pages):
    session = requests.Session()

    pageUrl = 'https://www.ptt.cc/bbs/'+kanban+'/index.html'
    pageCounter = 1
    while pageCounter <= pages:
        response = session.get(pageUrl, cookies={'over18': '1'})
        bsObj = BeautifulSoup(response.text, "html.parser")

        articles = bsObj.findAll("div", {"class": "r-ent"})

        articlesList = []
        for article in articles:
            articleInfo = {}

            author = article.find("div", {"class": "author"})
            date = article.find("div", {"class": "date"})
            title = article.find("div", {"class": "title"})

            articleInfo['author'] = author.get_text()
            articleInfo['date'] = date.get_text()
            articleInfo['title'] = title.get_text()
            articleInfo['kanban'] = kanban
            articleInfo['content'] = ''
            articleInfo['url'] = "https://www.ptt.cc"+article.find('a')['href']

            articlesList.append(articleInfo)

        u = bsObj.select("div.btn-group.btn-group-paging a")
        pageUrl = "https://www.ptt.cc" + u[1]["href"]
        pageCounter += 1

    return articlesList

def fetchContent(articles):

    session = requests.Session()

    for article in articles:
        response = session.get(article['url'], cookies={'over18': '1'})

        bsObj = BeautifulSoup(response.text, "html.parser")

        metas = bsObj.findAll("div", {"class": "main-content"}, text=True, recursive=False) 

        content = metas[0].get_text()

        articles['content'] = content

articlesList = fetchUrlList('Gossiping', 2)
articlesList = fetchContent(articlesList)

print(articlesList)