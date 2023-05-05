from datetime import date
from django.test import TestCase
from unittest.mock import patch
from apps.data_collection.crawler.yeonhap_article_crawler import YeonhapArticleCrawler


class TestYeonhapArticleCrawler(TestCase):


    def setUp(self):
        self.crawler = YeonhapArticleCrawler()

    def tearDown(self):
        self.crawler.driver.stop()    

    @patch('apps.data_collection.crawler.chrome_driver.ChromeDriver')
    def test_get_articles(self, mock_driver):
        mock_driver_instance = mock_driver.return_value
        mock_driver_instance.get_driver.return_value = mock_driver_instance
        mock_driver_instance.find_element.return_value = type('WebElement', (object,), {'text': 'Test Title'})
        mock_driver_instance.find_elements.return_value = [type('WebElement', (object,), {'text': 'Test Content'})]
        links = ['https://v.daum.net/v/20230504113522195?f=o']
        crawler = YeonhapArticleCrawler()
        result = crawler.get_articles(links)
        expected = [{
            'title': "'마약음료' 일당 구속기소…'최대 사형' 혐의 적용",
            'content': '[연합뉴스 자료사진](서울=연합뉴스) 박형빈 기자 = 검찰이 강남 학원가 \'마약 음료\'를 제조·공급한 보이스피싱 조직원 일당 3명을 재판에 넘겼다.검찰은 특히 최고 사형까지 구형할 수 있는 마약류관리법상 \'영리목적 미성년자 마약 투약\' 혐의를 적용했다.서울중앙지검 전담수사팀(신준호 부장검사)은 4일 마약류관리법 위반 및 범죄단체가입·활동 등 혐의로 마약 음료 제조·공급자 길모 씨와 보이스피싱 전화중계기 관리책 박모 씨를 구속기소 했다.별건의 마약 판매 혐의로 이미 구속기소 된 전달책 박모 씨는 길씨에게 마약을 전달한 혐의로 추가 기소됐다.이들은 중국 소재 보이스피싱 조직과 공모해 마약 음료를 제조, \'집중력 강화 음료 무료 시음회\'를 빙자해 강남 학원가에서 제공한 것으로 드러났다.길씨는 지정된 장소에 마약을 가져다 두는 이른바 \'던지기 수법\'으로 박씨로부터 얻은 필로폰 10g을 우유와 섞어 직접 마약 음료 100병을 제조, 미성년자 13명에게 준 혐의를 받는다.이 가운데 9명이 실제로 마약 음료를 마셨고, 그 가운데 6명은 환각 등 증상을 겪은 것으로 검찰은 파악했다.애초 경찰은 법정 최고형이 무기징역인 \'미성년자 마약제공\' 혐의로 길씨를 송치했지만, 검찰은 한층 중한 \'영리목적 미성년자 마약투약\' 혐의를 적용했다.마약류 관리에 관한 법률은 영리를 목적으로 미성년자에게 마약을 상습적으로 수수·조제·투약·제공한 자에게는 사형·무기징역 또는 10년 이상의 징역에 처하도록 한다.아울러 검찰은 마약 음료를 복용한 피해자들이 환각 증세를 보인 것에 대해서는 길씨에게 특수상해 혐의를 적용했다.피해자의 부모 6명에게 \'자녀를 마약 투약 혐의로 신고하겠다\'고 협박해 금품을 요구한 혐의(공갈미수)도 있다.김씨는 일당이 피해 학부모에게 협박 전화를 거는 과정에서 중계기를 이용해 070으로 시작하는 중국 인터넷전화 번호를 국내 휴대전화 번호(010)로 변작해준 혐의를 받는다. 차명 계좌로 범죄 수익 1천542만원을 입금받아 자금을 세탁한 혐의도 있다.검찰은 사건 송치 이후 길씨 등과 통화한 300여명의 대한 계좌거래·출입국 내역 등을 분석해 추가로 보이스피싱 조직원 모집책 이모씨를 국내에서 검거, 이달 2일 체포해 구속영장을 청구했다.이씨의 구속 전 피의자 심문(영장심사)은 5일 오후 서울중앙지법 이용제 판사 심리로 열릴 예정이다.검찰은 중국 공안 등과 공조해 보이스피싱 총책을 비롯한 국내·외 추가 공범에 대한 수사에 나선다는 방침이다.검찰은 "불특정 청소년을 속여 마약 음료를 투약하고 갈취 수단으로 활용한 신종 보이스피싱 범죄"라며 "죄질에 상응하는 처벌이 이뤄지도록 철저하게 공소를 유지하고, 범죄수익을 끝까지 추적해 환수하겠다"고 밝혔다.binzz@yna.co.kr제보는 카카오톡 okjebo\n<저작권자(c) 연합뉴스, 무단 전재-재배포 금지> 2023/05/04 11:33 송고', 
            'written_at': date(2023, 5, 4),
            'url': 'https://v.daum.net/v/20230504113522195?f=o'
        }]
        self.assertEqual(result, expected)