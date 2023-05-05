from django.test import TestCase, Client
from django.urls import reverse
from django.core.management import call_command
from apps.data_api.models import *
from apps.data_collection.models import *
from apps.web_pages.constants import *

# Create your tests here.

"""
1. 데이터가 없을 때
2. words 모델에 마약 내용이 없을 때
3. 정상작동할 때
"""

class DrugListViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('web:list')

        call_command('loaddata', 'test_drug.json')
        call_command('loaddata', 'test_article.json')
        call_command('loaddata', 'test_word.json')
    
    def test_without_data(self):
        Drug.objects.all().delete()

        response = self.client.get(self.url)
        content = str(response.content.decode('utf-8'))
        status = response.status_code
        self.assertEqual(status, 200)
        self.assertTrue(LIST_CREATION_REJECT in content)

    def test_drugs_not_in_words(self):
        article_id = Article.objects.first()
        Word.objects.all().delete()
        word = Word(article_id=article_id, text='', frequency=1)
        word.save()
        
        response = self.client.get(self.url)
        content = response.content.decode('utf-8')
        status = response.status_code
        self.assertEqual(status, 200)
        self.assertTrue(LIST_CREATION_FAILED in content)

    def test_work_successfully(self):
        article_id = Article.objects.first()
        word = Word(article_id=article_id, text='펜타닐', frequency=1)
        word.save()

        response = self.client.get(self.url)
        content = response.content.decode('utf-8')
        status = response.status_code
        self.assertEqual(status, 200)
        self.assertTrue("list-group" in content)
        
