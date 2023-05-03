from django.test import TestCase
from apps.data_collection.views import *
from apps.data_collection.models import *

class CollectionTest(TestCase):
    @classmethod
    def test_save_article(self):
        save_article()
        instances = Article.objects.all()
        print(f"전체 saved 된 데이터 : {instances}")
        for i, instance  in enumerate(instances) :
            print(f"|-----check [{i}]------|")
            print(instance.article_id)
            print(instance.title)
            # print(instance.content)
            print(instance.written_at)
            print(instance.url)
            print(instance.created_at)

'''
테스트 실행 명령어 :
manage.py test apps.data_collection.tests.tests_views
'''