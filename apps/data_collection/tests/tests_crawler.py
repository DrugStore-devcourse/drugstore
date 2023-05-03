from django.test import TestCase
from apps.data_collection.articleCrawler import ArticleCrawler

class ArticleCrawlerTest(TestCase):
    @classmethod
    # def test_init_crawler(self):
    #     crawler =ArticleCrawler() 
    #     print("실행됨")

    def test_get_chosun_article(self):
        sample_chosun = {'chosun': ['https://v.daum.net/v/20230501032327247?f=o', 'https://v.daum.net/v/20230501170112518?f=o', 'https://v.daum.net/v/20230501110534799?f=o', 'https://v.daum.net/v/20230501035254269?f=o', 'https://v.daum.net/v/20230501224248386?f=o', 'https://v.daum.net/v/20230501234715680?f=o', 'https://v.daum.net/v/20230501070028861?f=o'], 'yeonhap': ['https://v.daum.net/v/20230501162049544?f=o', 'https://v.daum.net/v/20230501152406049?f=o', 'https://v.daum.net/v/20230501104010097?f=o', 'https://v.daum.net/v/20230501095825982?f=o', 'https://v.daum.net/v/20230501140008285?f=o', 'https://v.daum.net/v/20230501110054663?f=o', 'https://v.daum.net/v/20230501163258812?f=o', 'https://v.daum.net/v/20230501135820240?f=o', 'https://v.daum.net/v/20230501093121299?f=o', 'https://v.daum.net/v/20230501162632660?f=o', 'https://v.daum.net/v/20230501110007583?f=o']}
        crawler = ArticleCrawler() 
        crawler.get_chosun_article(sample_chosun['chosun'][0])