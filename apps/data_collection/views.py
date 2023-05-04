import logging
from apps.data_collection.crawler.article_crawler import ArticleCrawler
from apps.data_collection.crawler.chosun_article_crawler import ChosunArticleCrawler
from .constants import PRESSES
from .models import *

def save_articles():
    '''
    This function saves article data crawled using the 'ArticleCrawler' class to the database.

    <<TODO>> 예외처리, 로깅 등 
    <<TODO>> 언론사 2개 추가 구현  
    '''
    logger = logging.getLogger('crawlerlogger')
    
    crawler = ArticleCrawler() 
    article_links = crawler.get_article_links(PRESSES)
    
    # Get aritcles of 'chosun' press and Save them
    chosun_crawler = ChosunArticleCrawler()
    chosun_articles = chosun_crawler.get_articles(article_links['chosun'])
    for article in chosun_articles:
        new_article = Article(**article)
        new_article.save()
