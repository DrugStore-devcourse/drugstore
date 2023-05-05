from datetime import date
from unittest.mock import patch, Mock
from django.test import TestCase
from apps.data_collection.crawler.kbs_article_crawler import KbsArticleCrawler


class TestKbsArticleCrawler(TestCase):


    def setUp(self):
        self.crawler = KbsArticleCrawler()

    def tearDown(self):
        self.crawler.driver.stop()

    @patch('apps.data_collection.crawler.chrome_driver.ChromeDriver')
    def test_get_articles(self, mock_driver):
        mock_driver_instance = mock_driver.return_value
        mock_driver_instance.get_driver.return_value = mock_driver_instance
        mock_driver_instance.find_element.return_value = type('WebElement', (object,), {'text': 'Test Title'})
        mock_driver_instance.find_elements.return_value = [type('WebElement', (object,), {'text': 'Test Content'})]
        links = ['https://v.daum.net/v/20230503065139459?f=o']
        crawler = KbsArticleCrawler()
        result = crawler.get_articles(links)
        expected = [{
            'title': 'SNS로 마약 거래, 외국인 무더기 검거',
            'content': '[앵커]\n\n남해안 일대에서 마약을 투약하거나 공급한 외국인 15명이 무더기로 경찰에 붙잡혔습니다.\n\n이들은 현지인들이 주로 쓰는 SNS를 통해 마약을 거래했고, 본국을 오가는 사람을 활용해 마약을 국내로 반입했습니다.\n\n보도에 김민지 기자입니다.\n\n[리포트]\n\n해경 경비함정이 바지선 옆 소형 선박에 다가가고 선별 작업을 하던 외국인 노동자를 체포합니다.\n\n동전 빨래방에 들이닥친 경찰은 저항하던 외국인을 붙잡습니다.\n\n차량 4대가 도로 위에 서 있던 승용차 한 대를 에워쌉니다.\n\n["다리, 다리, 잡아."]\n\n경찰차를 추돌한 뒤 도주하려던 남성을 붙잡기 위해 도로에서 몸싸움이 벌어집니다.\n\n통영해경이 마약류인 엑스터시와 케타민 등을 복용하거나 공급한 혐의로 외국인 15명을 붙잡았습니다.\n\n유통 총책 2명과 중간 판매책 등 5명은 구속 송치됐습니다.\n\n이들은 주로 우편이나 본국을 오가는 사람들을 이른바 \'지게꾼\'으로 이용해 국내로 마약을 들여왔습니다.\n\n대구에서 활동하는 상위 유통책을 통해 김해·부산의 중간 판매책에게 마약을 공급하면 중간 판매책들은 거제 지역 하위 판매책들에게 공급하는 방식이었습니다.\n\n외국인들은 주로 노래주점이나 외국인 전용 클럽 등에서 마약을 투약했습니다.\n\n[이정석/통영해양경찰서 수사과장 : "일하면서 힘든 노동과 고향에 대한 향수, 이런 것들 때문에 자기 나라 사람들끼리 모여서 마약을 투약했다고 (진술하고 있습니다)."]\n\n거래 대금은 현금 던지기 수법이 활용됐습니다.\n\n텔레그램 외에도 현지인들이 주로 쓰는 SNS를 통해 마약을 거래했고, 경찰은 상위 유통책의 SNS 아이디를 확보해 일당을 검거할 수 있었습니다.\n\n해경은 조선소와 양식장이 밀집한 남해안 일대를 중심으로 외국인 마약 유통조직이 더 있을 것으로 보고 수사를 확대하고 있습니다.\n\nKBS 뉴스 김민지입니다.\n\n촬영기자:최현진',
            'written_at': date(2023, 5, 3),
            'url': 'https://v.daum.net/v/20230503065139459?f=o'
        }]
        self.assertEqual(result, expected)