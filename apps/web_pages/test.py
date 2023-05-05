from django.test import TestCase, Client
from django.urls import reverse
from ..data_api.models import *
from ..data_collection.models import *
from django.core.management import call_command

# Create your tests here.

"""
1. 데이터가 없을 때
2. words 모델에 마약 내용이 없을 때
3. 정상작동할 때
"""

class DrugListViewTest(TestCase):
    def setUp(self):
        self.url = reverse('web:list')
        self.client = Client()

        call_command('loaddata', 'test_drug.json')
        call_command('loaddata', 'test_article.json')
        call_command('loaddata', 'test_word.json')
    
    def test_without_data(self):
        Drug.objects.all().delete()

        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, LIST_CREATION_REJECT)

    def test_drugs_not_in_words(self):
        article_id = Article.objects.first().values()['article_id']
        Words.objects.all().delete()
        word = Words(article_id=article_id, text='', frequency=1)
        word.save()
        
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, LIST_CREATION_FAILED)

    def test_work_successfully(self):
        response = self.client.get(self.url)
        
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "result")
        
