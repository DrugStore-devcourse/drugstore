from datetime import date
from unittest.mock import patch
from django.test import TestCase
from apps.data_collection.crawler.chosun_article_crawler import ChosunArticleCrawler


class TestChosunArticleCrawler(TestCase):


    def setUp(self):
        self.crawler = ChosunArticleCrawler()

    def tearDown(self):
        self.crawler.driver.stop()

    @patch('apps.data_collection.crawler.chrome_driver.ChromeDriver')
    def test_get_articles(self, mock_driver):
        mock_driver_instance = mock_driver.return_value
        mock_driver_instance.get_driver.return_value = mock_driver_instance
        mock_driver_instance.find_element.return_value = type('WebElement', (object,), {'text': 'Test Title'})
        mock_driver_instance.find_elements.return_value = [type('WebElement', (object,), {'text': 'Test Content'})]
        links = ['https://v.daum.net/v/20230503144403510?f=o']
        crawler = ChosunArticleCrawler()
        result = crawler.get_articles(links)
        expected = [{
            'title': '‘작전명 스펙터’ 9國 연합 마약전쟁... 850㎏·700억원 압수했다',
            'content': '3개 대륙, 9개국, 29개 기관의 정예 수사 인력들이 참여한 사상 최대규모의 국제 마약범죄 퇴치작전인 스펙터 작전(Operation SpecTor)이 전세계에서 288명의 마약사범을 검거하고 850㎏의 마약과 700억원 넘는 검은돈을 압수하는 성과를 거뒀다. 무장한 마약사범 등이 갖고 있던 총기 117정도 확보했다. 마약사범들의 수법이 갈수록 지능화되고 마약이 걷잡을 수 없이 확산하면서 이와 같은 국제 공조 퇴치작전이 앞으로도 전개될 것이라는 전망이 나온다.미 연방법무부와 연방수사국(FBI), 유로폴 등 참여 기관들이 2일(현지 시각) 이번 작전 성과를 발표했다. 우선 이번 작전을 통해 다크넷을 활용해 마약 밀매와 공급에 연루된 혐의를 받는 288명을 체포해 신병을 확보했다. 이 중 53%(153명)가 미국에서 붙잡혔으며 영국(55명), 독일(52명), 네덜란드(10명)순으로 체포된 용의자 숫자가 많았다. 다크넷이란 표준 프로토콜과 포트를 사용하지 않고 IP 주소도 공유않는 익명의 인터넷 공간으로 일반적으로 마약과 인신매매 등 강력범죄에 활용된다. 암페타민 258㎏, 코카인과 MDMA 각 43㎏, LSD와 엑스터시 알약 각 10㎏ 등을 포함한 850㎏의 마약도 몰수했다. 무장한 마약조직원들로부터 총기 117정을 확보한 것도 성과로 꼽힌다. 마약 거래에 연루된 ‘검은돈’ 역시 현금과 가상화폐를 합쳐 5340만 달러(약 714억원)에 달한다.미 법무부는 이번 작전에 대해 “지금까지 실행됐던 마약관련 국제공조 수사 중엔서 가장 큰 규모로 펼쳐졌다”고 밝혔다. 앞서 지난 2021년에도 FBI와 유로폴 등이 협업해 10개월동안 진행한 공조수사를 통해 거둔 성과(150여명 체포·마약 234㎏ 압수)를 뛰어넘는 규모다. 미국은 최근 마약성 진통제 오피오이드 오·남용 문제로 사망자가 급증하면서 다크넷 등을 이용한 국제 마약 거래망을 분쇄하기 위한 해외 공조 수사에 주력해왔다. 이번 ‘스펙터 작전’은 다국적 수사기관이 협업한 다섯번째 작전이다. 이번 작전에는 연방 법무부·국방부·FBI·DEA(마약수사국)·ICE(이민세관국)·FDA(식품의약국)·해군범죄수사국(NCIS) 등 12개 수사기관이 참가했다.해외에서도 유로폴을 비롯해 국립범죄수사국(영국)· 연방수사청(오스트리아)·프랑크푸르트 연방검찰과 베를린 경찰(독일)·국립경찰(네덜란드)·중앙범죄수사국(폴란드)·연방경찰(브라질) 등도 참여했다. 체포된 용의자에 대한 수사와 기소가 속속 진행되면서 중형 선고가 내려지는 사례도 나왔다. 2021년 5월부터 2022년 5월 사이에 다크넷을 통해 가상화폐로 펜타닐·메스암페타민·헤로인 등 마약을 확보한 뒤 우편물로 미국 전역에 공급하려다 적발된 플로리다 출신 마약사범 3명 중 2명에게 지난해 12월 각각 징역 16년과 징역 11년이 선고됐으며, 나머지 한 명은 곧 선고를 앞두고 있다. 이들과 거래하는 고객 명단은 미국 전역에 6000여명에 달한 것으로 알려졌다.미국에서 마약 범죄는 국가 기강을 송두리째 흔드는 최대의 위협으로 떠올랐다. 오피오이드 중독 관련 사망자는 2020년 5만7834명에서 2021년 7만1238명에서 1년새 15% 늘어날 정도로 폭증세다. 이에 따라 각국이 협업하는 ‘글로벌 마약과의 전쟁’도 더욱 큰 규모로 전개될 것이라는 전망이 나온다. 이번 작전에 참가한 기관 책임자와 담당자들도 모두 국제 공조 수사의 필요성을 강조했다.캐서린 드 볼 유로폴 국장은 “세 대륙에 걸친 사법기관들이 공조한 이번 작전은함께 할 때 더 나은 성과를 보여준다는 것을 보여줬다”며 “국제사법공조는 다크넷을 통한 범죄자들에게도 책임을 물을 수 있는 수단이 있다”고 말했다. 크리스토퍼 레이 FBI 국장은 “이번 작전은 왜 우리가 문제 해결을 위해 해외 파트너들과 협력해야 하는지를 보여줬다”고 했다. 메릭 갈런드 미국 법무부장관(연방 검찰총장)은 “이번 공조 작전이 범죄집단에 주는 메시지는 명확하다”며 “인터넷에 접속해 최대한 검은돈을 꽁꽁 숨기려 해도 우리는 찾아내 책임을 물을 것이라는 것”이라고 했다.',
            'written_at': date(2023, 5, 3),
            'url': 'https://v.daum.net/v/20230503144403510?f=o'
        }]
        self.assertEqual(result, expected)