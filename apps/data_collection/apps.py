import logging
import sys

from django.apps import AppConfig
from django.core.management import call_command


class DataCollectionConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.data_collection'

    def ready(self):
        """
         runserver시 마약 뉴스 크롤링 커맨드를 수행
        """
        # only run during 'runserver' command
        if 'runserver' not in sys.argv:
            return

        # FIXME HTTP 연결 실패
        # call_command('crawldata')
