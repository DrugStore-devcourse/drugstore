from django.test import TestCase
from apps.data_collection.articleCrawler import ArticleCrawler

class ArticleCrawlerTest(TestCase):
    @classmethod
    # def test_init_crawler(self):
    #     crawler =ArticleCrawler() 
    #     print("실행됨")

    def test_get_article_links(self): 
        presses = {
        'chosun' : 'https://search.daum.net/search?w=news&q=%EB%A7%88%EC%95%BD&DA=STC&spacing=0&period=d&sd={{startdate}}&ed={{enddate}}&cp=16d4PV266g2j-N3GYq&cpname=%EC%A1%B0%EC%84%A0%EC%9D%BC%EB%B3%B4',
        'yeonhap' : 'https://search.daum.net/search?w=news&q=%EB%A7%88%EC%95%BD&DA=STC&spacing=0&period=d&sd={{startdate}}&ed={{enddate}}&cp=16X5Xh1MWS7Qt1sMrW&cpname=%EC%97%B0%ED%95%A9%EB%89%B4%EC%8A%A4',
        'kbs' : 'https://search.daum.net/search?nil_suggest=btn&w=news&DA=STC&cluster=y&q=%EB%A7%88%EC%95%BD&period=d&sd={{startdate}}&ed={{enddate}}&cp=16hWxJmTql2y9rxiuO&cpname=kbs'
        }
        crawler = ArticleCrawler() 
        article_links = crawler.get_article_links(presses)
        print(article_links)

    def test_get_chosun_article(self):
        sample_chosun = {'chosun': ['https://v.daum.net/v/20230501032327247?f=o', 'https://v.daum.net/v/20230501170112518?f=o', 'https://v.daum.net/v/20230501110534799?f=o', 'https://v.daum.net/v/20230501035254269?f=o', 'https://v.daum.net/v/20230501224248386?f=o', 'https://v.daum.net/v/20230501234715680?f=o', 'https://v.daum.net/v/20230501070028861?f=o'], 'yeonhap': ['https://v.daum.net/v/20230501162049544?f=o', 'https://v.daum.net/v/20230501152406049?f=o', 'https://v.daum.net/v/20230501104010097?f=o', 'https://v.daum.net/v/20230501095825982?f=o', 'https://v.daum.net/v/20230501140008285?f=o', 'https://v.daum.net/v/20230501110054663?f=o', 'https://v.daum.net/v/20230501163258812?f=o', 'https://v.daum.net/v/20230501135820240?f=o', 'https://v.daum.net/v/20230501093121299?f=o', 'https://v.daum.net/v/20230501162632660?f=o', 'https://v.daum.net/v/20230501110007583?f=o']}
        crawler = ArticleCrawler() 
        for link in sample_chosun['chosun']:
            print("=======================WERWRWEWERWER---")
            article = crawler.get_chosun_article(link)
            print(article)

'''
테스트 실행 명령어 :
manage.py test apps.data_collection.tests.tests_crawler
'''