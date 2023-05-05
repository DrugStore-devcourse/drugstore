from unittest import TestCase
from unittest.mock import patch, MagicMock
from apps.data_collection.crawler.article_crawler import ArticleCrawler
from apps.data_collection.constants import PRESSES

class TestArticleCrawler(TestCase):


    def setUp(self):
        self.crawler = ArticleCrawler()

    @patch('apps.data_collection.crawler.article_crawler.requests.get')
    def test_get_article_links_mock(self, mock_get):
        mock_response = '<html><body><div class="sub_expander"><span>1 / 2 건</span></div><ul class="list_news"><li><a href="https://example.com/article1">Article 1</a></li><li><a href="https://example.com/article2">Article 2</a></li></ul></body></html>'
        mock_get.return_value.text = mock_response
        expected_links = {
            'chosun': ['https://example.com/article1', 'https://example.com/article2'],
            'yeonhap': ['https://example.com/article1', 'https://example.com/article2'],
            'kbs': ['https://example.com/article1', 'https://example.com/article2']
        }
        self.assertEqual(self.crawler.get_article_links(PRESSES), expected_links)

    def test_get_article_links(self):
        self.crawler.get_article_links = MagicMock(return_value={
            'chosun': ['https://v.daum.net/v/20230504113701270?f=o', 'https://v.daum.net/v/20230504094011255?f=o', 'https://v.daum.net/v/20230504050130669?f=o', 'https://v.daum.net/v/20230504000130017?f=o'],
            'yeonhap': ['https://v.daum.net/v/20230504113522195?f=o', 'https://v.daum.net/v/20230504134916192?f=o', 'https://v.daum.net/v/20230504154927861?f=o', 'https://v.daum.net/v/20230504180013989?f=o', 'https://v.daum.net/v/20230504111812380?f=o', 'https://v.daum.net/v/20230504172645036?f=o', 'https://v.daum.net/v/20230504161519874?f=o', 'https://v.daum.net/v/20230504105830567?f=o', 'https://v.daum.net/v/20230504091616323?f=o', 'https://v.daum.net/v/20230504101916038?f=o', 'https://v.daum.net/v/20230504164719843?f=o', 'https://v.daum.net/v/20230504035839147?f=o', 'https://v.daum.net/v/20230504180011987?f=o', 'https://v.daum.net/v/20230504144333073?f=o', 'https://v.daum.net/v/20230504122746583?f=o', 'https://v.daum.net/v/20230504094220347?f=o', 'https://v.daum.net/v/20230504070509453?f=o'], 
            'kbs': ['https://v.daum.net/v/20230504192746350?f=o', 'https://v.daum.net/v/20230504105344376?f=o', 'https://v.daum.net/v/20230504185150375?f=o', 'https://v.daum.net/v/20230504143355724?f=o', 'https://v.daum.net/v/20230504161443836?f=o', 'https://v.daum.net/v/20230504215952677?f=o', 'https://v.daum.net/v/20230504080945305?f=o', 'https://v.daum.net/v/20230504194148646?f=o', 'https://v.daum.net/v/20230504055931418?f=o', 'https://v.daum.net/v/20230504192746350?f=o', 'https://v.daum.net/v/20230504105344376?f=o', 'https://v.daum.net/v/20230504185150375?f=o', 'https://v.daum.net/v/20230504143355724?f=o', 'https://v.daum.net/v/20230504161443836?f=o', 'https://v.daum.net/v/20230504215952677?f=o', 'https://v.daum.net/v/20230504080945305?f=o', 'https://v.daum.net/v/20230504194148646?f=o', 'https://v.daum.net/v/20230504055931418?f=o']
        })
        expected_result = {
            'chosun': ['https://v.daum.net/v/20230504113701270?f=o', 'https://v.daum.net/v/20230504094011255?f=o', 'https://v.daum.net/v/20230504050130669?f=o', 'https://v.daum.net/v/20230504000130017?f=o'],
            'yeonhap': ['https://v.daum.net/v/20230504113522195?f=o', 'https://v.daum.net/v/20230504134916192?f=o', 'https://v.daum.net/v/20230504154927861?f=o', 'https://v.daum.net/v/20230504180013989?f=o', 'https://v.daum.net/v/20230504111812380?f=o', 'https://v.daum.net/v/20230504172645036?f=o', 'https://v.daum.net/v/20230504161519874?f=o', 'https://v.daum.net/v/20230504105830567?f=o', 'https://v.daum.net/v/20230504091616323?f=o', 'https://v.daum.net/v/20230504101916038?f=o', 'https://v.daum.net/v/20230504164719843?f=o', 'https://v.daum.net/v/20230504035839147?f=o', 'https://v.daum.net/v/20230504180011987?f=o', 'https://v.daum.net/v/20230504144333073?f=o', 'https://v.daum.net/v/20230504122746583?f=o', 'https://v.daum.net/v/20230504094220347?f=o', 'https://v.daum.net/v/20230504070509453?f=o'], 
            'kbs': ['https://v.daum.net/v/20230504192746350?f=o', 'https://v.daum.net/v/20230504105344376?f=o', 'https://v.daum.net/v/20230504185150375?f=o', 'https://v.daum.net/v/20230504143355724?f=o', 'https://v.daum.net/v/20230504161443836?f=o', 'https://v.daum.net/v/20230504215952677?f=o', 'https://v.daum.net/v/20230504080945305?f=o', 'https://v.daum.net/v/20230504194148646?f=o', 'https://v.daum.net/v/20230504055931418?f=o', 'https://v.daum.net/v/20230504192746350?f=o', 'https://v.daum.net/v/20230504105344376?f=o', 'https://v.daum.net/v/20230504185150375?f=o', 'https://v.daum.net/v/20230504143355724?f=o', 'https://v.daum.net/v/20230504161443836?f=o', 'https://v.daum.net/v/20230504215952677?f=o', 'https://v.daum.net/v/20230504080945305?f=o', 'https://v.daum.net/v/20230504194148646?f=o', 'https://v.daum.net/v/20230504055931418?f=o']
        }

        result = self.crawler.get_article_links(PRESSES)
        self.assertEqual(result, expected_result)
