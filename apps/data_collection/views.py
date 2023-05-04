import logging
from konlpy.tag import Kkma
from apps.data_collection.crawler.article_crawler import ArticleCrawler
from apps.data_collection.crawler.chosun_article_crawler import ChosunArticleCrawler
from django.core.exceptions import ValidationError
from django.db import transaction
from .constants import PRESSES
from .models import *

logger = logging.getLogger('crawlerlogger')

def save_articles():
    '''
    This function saves article data crawled using the 'ArticleCrawler' class to the database.

    <<TODO>> 예외처리, 로깅 등 
    <<TODO>> 언론사 2개 추가 구현  
    '''
    crawler = ArticleCrawler() 
    article_links = crawler.get_article_links(PRESSES)
    
    # Get aritcles of 'chosun' press and Save them
    chosun_crawler = ChosunArticleCrawler()
    chosun_articles = chosun_crawler.get_articles(article_links['chosun'])
    for article in chosun_articles:
        new_article = Article(**article)
        new_article.save()

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
