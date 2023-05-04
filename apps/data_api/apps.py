import logging
import sys

from django.db import OperationalError

from django.apps import AppConfig
from django.core.management import call_command

from apps.data_api.constants import DRUG_TABLE_NOT_EXIST


class DataApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.data_api'

    def ready(self):
        """
         runserver시 drug data를 load 한다
        """

        # only run during 'runserver' command
        if 'runserver' not in sys.argv:
            return

        try:
            # ready 실행시 Drug 모델이 생성이 안될 수 있어 함수 내부에서 호출
            from .models import Drug

            if Drug.objects.exists():
                Drug.objects.all().delete()
                
            call_command('loaddata', 'drug.json')
        except OperationalError:
            logging.warning(DRUG_TABLE_NOT_EXIST)
            raise OperationalError(DRUG_TABLE_NOT_EXIST)
