from django.test import TestCase
from apps.data_collection.views import *
from apps.data_collection.models import *

class CollectionTest(TestCase):
    @classmethod
    def test_save_article(self):
        save_articles()
        instances = Article.objects.all()
        print(f"전체 saved 된 데이터 : {instances}")
        for i, instance  in enumerate(instances) :
            print(f"|-----check [{i}]------|")
            print(f'|--- id : {instance.article_id}')
            print(f'|--- title : {instance.title}')
            print(f'|--- written_at : {instance.written_at}')
            print(f'|--- url : {instance.url}')
            print(f'|--- created_at : {instance.created_at}')
            print(f'|--- content : {instance.content}')

'''
테스트 실행 명령어 :
manage.py test apps.data_collection.tests.test_views
'''