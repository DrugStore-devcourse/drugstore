import json

from django.apps import AppConfig
from django_seed import Seed
from django.core.management import call_command


class DataApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.data_api'

    def ready(self):
        # 서버가 실행될 때 Drug 모델에 데이터 생성
        from .models import Drug
        if Drug.objects.exists():
            Drug.objects.all().delete()

        call_command('loaddata', 'drug.json')
