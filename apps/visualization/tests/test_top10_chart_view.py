from django.test import TestCase, Client
from django.urls import reverse
from django.core.management import call_command
from django.http import Http404
from django.db import connection
from apps.data_api.models import Drug
from apps.data_collection.models import Article, Word
from apps.visualization.constants import TOP10_PIE_CHART, APP_NAME, CHART_CREATION_REJECT, CHART_CREATION_FAILED


class Top10PieChartViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse(f'{APP_NAME}:{TOP10_PIE_CHART}')

        call_command('loaddata', 'test_drug.json')
        call_command('loaddata', 'test_article.json')
        call_command('loaddata', 'test_word.json')

    def tearDown(self):
        Drug.objects.all().delete()
        Article.objects.all().delete()
        Word.objects.all().delete()

    def test_datas_not_exists(self):
        """
        데이터가 없을 경우 200 및 에러 메세지 조회
        :return:
        """
        Drug.objects.all().delete()

        response = self.client.get(self.url)
        response.content = response.content.decode('utf-8')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, CHART_CREATION_REJECT)

    def test_successfully_renders_chart(self):
        """
        차트 랜더링이 성공한 경우 200 ok 및 특정 태그 조회
        :return:
        """
        response = self.client.get(self.url)
        response.content = response.content.decode('utf-8')
        expected_html = '<title>Awesome-pyecharts</title>'
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, expected_html)

    def test_if_drug_or_word_table_not_exist_raise_404(self):
        """
        테이블이 없는 경우 404 조회
        :return:
        """
        table_names = connection.introspection.table_names()
        if 'drugs' not in table_names or 'words' not in table_names:
            response = self.client.get(self.url)
            response.content = response.content.decode('utf-8')

            self.assertEqual(response.status_code, 404)
            self.assertRaises(Http404)
            self.assertContains(response, CHART_CREATION_FAILED)
