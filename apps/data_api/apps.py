import logging
from sqlite3 import OperationalError
from django.db.utils import OperationalError

from django.apps import AppConfig
from django.core.management import call_command

logger = logging.getLogger(__name__)


class DataApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.data_api'

    def ready(self):
        # ready 실행시 Drug 모델이 생성안될 수 있어 내부에서 호출
        from .models import Drug

        try:
            if Drug.objects.exists():
                Drug.objects.all().delete()
                call_command('loaddata', 'drug.json')
        except OperationalError:
            logger.warning("[drugs 데이터 생성 실패] drugs 테이블이 없습니다 migrate를 수행해주세요")
