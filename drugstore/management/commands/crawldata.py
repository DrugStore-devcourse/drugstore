import logging

from django.core.management.base import BaseCommand
from apps.data_collection.models import *
from apps.data_collection.views import save_articles, parse_article_to_word


class Command(BaseCommand):
    help = 'Crawl drug news data.'

    def handle(self, *args, **options):
        logging.info('delete words and article')
        Word.objects.all().delete()
        Article.objects.all().delete()

        logging.info('run drug news crawler')
        save_articles()
        parse_article_to_word()

        self.stdout.write(self.style.SUCCESS('Successfully loaded crawl data.'))
