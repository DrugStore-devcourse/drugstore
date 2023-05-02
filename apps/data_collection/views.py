from django.shortcuts import render
from .models import *
from bs4 import BeautifulSoup
import requests
from datetime import datetime, timedelta

presses = {
    'chosun' : 'https://search.daum.net/search?w=news&q=%EB%A7%88%EC%95%BD&DA=STC&spacing=0&period=d&sd={{startdate}}&ed={{enddate}}&cp=16d4PV266g2j-N3GYq&cpname=%EC%A1%B0%EC%84%A0%EC%9D%BC%EB%B3%B4',
    'yeonhap' : 'https://search.daum.net/search?w=news&q=%EB%A7%88%EC%95%BD&DA=STC&spacing=0&period=d&sd={{startdate}}&ed={{enddate}}&cp=16X5Xh1MWS7Qt1sMrW&cpname=%EC%97%B0%ED%95%A9%EB%89%B4%EC%8A%A4',
    'kbs' : 'https://search.daum.net/search?nil_suggest=btn&w=news&DA=STC&cluster=y&q=%EB%A7%88%EC%95%BD&period=d&sd={{startdate}}&ed={{enddate}}&cp=16hWxJmTql2y9rxiuO&cpname=kbs'
}

def get_article_links() -> dict: 
    '''
    This function gets links to drug-related news articles from each press from the previous day.
    '''
    article_links = {}

    for press in presses : 
        article_links[press] = []
        today = datetime.today().strftime('%Y%m%d')
        yesterday = (datetime.today() - timedelta(days=1)).strftime('%Y%m%d')
        presses[press] = presses[press].replace('{{startdate}}', yesterday + "000000")
        presses[press] = presses[press].replace('{{enddate}}', today + "000000")

        res = requests.get(presses[press])
        soup = BeautifulSoup(res.text, "html.parser")

        # 페이지 계산 
        num_aritcle = int(soup.find("div" , "sub_expander").span.text.split('/ ')[1].split("건")[0])
        if num_aritcle > 1 :
            pages = (num_aritcle - 1)  // 10 
        else : 
            pages = 0
        pages += 1

        # 페이지 별 링크 가져옴
        for p in range(1, pages+1) : 
            res = requests.get(presses[press] + "&p=" + str(p))
            soup = BeautifulSoup(res.text, "html.parser")
            articles = soup.find("ul" , "list_news").find_all("li")
            for article in articles: 
                link = article.find("a").get('href')
                article_links[press].append(link)
    return article_links


def main() :
    article_links = get_article_links()
