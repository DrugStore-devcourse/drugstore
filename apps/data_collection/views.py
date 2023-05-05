import logging
from konlpy.tag import Kkma
from apps.data_collection.crawler.article_crawler import ArticleCrawler
from apps.data_collection.crawler.chosun_article_crawler import ChosunArticleCrawler
from apps.data_collection.crawler.kbs_article_crawler import KbsArticleCrawler
from apps.data_collection.crawler.yeonhap_article_crawler import YeonhapArticleCrawler
from django.core.exceptions import ValidationError
from django.db import transaction
from .constants import PRESSES
from .models import *

logger = logging.getLogger('crawlerlogger')

def save_articles():
    '''
    This function saves article data crawled using the 'ArticleCrawler' class to the database.
    - Get aritcles of 'chosun'/'yeonhap/'kbs' press and Save them
    '''
    crawler = ArticleCrawler() 
    article_links = crawler.get_article_links(PRESSES)
    articles = []
    if 'chosun' in article_links.keys():
        chosun_crawler = ChosunArticleCrawler()
        articles.extend(chosun_crawler.get_articles(article_links['chosun']))
    if 'yeonhap' in article_links.keys():
        yeonhap_crawler = YeonhapArticleCrawler()
        articles.extend(yeonhap_crawler.get_articles(article_links['yeonhap']))
    if 'kbs' in article_links.keys():
        kbs_crawler = KbsArticleCrawler()
        articles.extend(kbs_crawler.get_articles(article_links['kbs']))
    
    with transaction.atomic():
        for article in articles:
            article_url = article['url']
            new_article = Article(**article)
            try:
                new_article.full_clean()
                new_article.save()
            except ValidationError as e:
                logger.warning(f'Validation error occurred while saving the article: {article_url} {e}')

def parse_article_to_word():
    '''
    This function parses article contents to word using Konlpy and save word to database.
    '''
    articles = Article.objects.all()
    for article in articles :
        kkma = Kkma()
        words = kkma.nouns(article.content)
        for text in words:
            try:
                save_word(article, text)
            except Exception as e:
                logger.error(f"Error occurred while parsing article {article.article_id} to word: {str(e)}")

@transaction.atomic
def save_word(article, text:str):
    '''
    This function receives the article object and text and stores them in the Word model.

    :param article: Article - Instance of Article model
    :param text: str - A text word to save 
    '''
    try:
        word, created = Word.objects.get_or_create(article_id=article, text=text)
    except ValidationError:
        raise ValueError
    except Exception as e:
        logger.error(f'Error occurred while save word from article {article}: {str(e)}')
        raise ValueError
    if not created:
        word.frequency += 1
        word.save()
    return word
