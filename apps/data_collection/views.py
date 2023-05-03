from .models import *
from apps.data_collection.articleCrawler import ArticleCrawler

def save_article():
    '''
    This function saves article data crawled using the 'ArticleCrawler' class to the database.

    <<TODO>> 예외처리, 로깅 등 
    <<TODO>> 언론사 2개 추가 구현  
    '''
    presses = {
        'chosun' : 'https://search.daum.net/search?w=news&q=%EB%A7%88%EC%95%BD&DA=STC&spacing=0&period=d&sd={{startdate}}&ed={{enddate}}&cp=16d4PV266g2j-N3GYq&cpname=%EC%A1%B0%EC%84%A0%EC%9D%BC%EB%B3%B4',
        'yeonhap' : 'https://search.daum.net/search?w=news&q=%EB%A7%88%EC%95%BD&DA=STC&spacing=0&period=d&sd={{startdate}}&ed={{enddate}}&cp=16X5Xh1MWS7Qt1sMrW&cpname=%EC%97%B0%ED%95%A9%EB%89%B4%EC%8A%A4',
        'kbs' : 'https://search.daum.net/search?nil_suggest=btn&w=news&DA=STC&cluster=y&q=%EB%A7%88%EC%95%BD&period=d&sd={{startdate}}&ed={{enddate}}&cp=16hWxJmTql2y9rxiuO&cpname=kbs'
    }

    crawler = ArticleCrawler() 
    article_links = crawler.get_article_links(presses)

    for link in article_links['chosun'] : 
        article = crawler.get_chosun_article(link)
        new_article = Article( **article )
        new_article.save()

