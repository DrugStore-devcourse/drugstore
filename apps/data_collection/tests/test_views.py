from konlpy.tag import Kkma
from datetime import datetime,date
from django.test import TestCase
from unittest.mock import patch, call
from apps.data_collection.models import Article, Word
from apps.data_collection.views import save_articles, parse_article_to_word, save_word

class ArticleTestCase(TestCase):
    def setUp(self):
        self.articles_chosun_data = [
            # chosun
            { 
                "title": "케타민 20만명분 밀수한 마약 조직 운반책 2명 구속기소",
                "content": "‘클럽 마약’으로 불리는 케타민 20만명 투 약분을 밀수한 마약 조직원 2명이 재판에 넘겨졌다. 올해 초부터 시작된 관련 수사로 검찰이 적발한 조직원은 10명이 넘는다.3일 검찰에 따르면, 서울중앙지검 강력범죄수사부는 케타민 밀수 조직 운반책으로 활동한 20대 A씨 등 2명을 특정범죄가중법과 범죄단체 가입 등 혐의로 최근 구속기소했다.일당은 조직 차원에서 현지 태국 마약상과 접촉해 대량으로 사들인 케타민을 각각 5.4㎏과 1.8㎏씩 인천국제공항을 통해 몰래 들여온 것으로 조사됐다. A씨 등 운반책들은 비닐랩으로 감싼 케타민을 속옷 안에 숨기는 방식으로 밀수한 것으로 조사됐다.작년 말 케타민 밀수조직 범죄첩보를 입수해 수사해 온 검찰은 최근까지 이 사건과 관련해 현 재까지 총 15명을 검거했다. 검찰은 검거한 조직원들 대부분이 밀수에 가담한 것으로 보고, 판매책 검거에 수사력을 집중하고 있는 것으로 전해졌다.케타민은 의료용 또는 동물용 마취제의 일종으로, 젊은 층 사이에서 ‘클럽 마약’으로 불린다. 케타민은 필로폰이나 코카인보다 싸게 구입할 수 있고 술이나 음료에 타서 마실 수 있다. 다른 사람 음료에도 몰래 타기 쉬워 피해 발생 우 려가 큰 마약이다.",
                "url": "https://v.daum.net/v/20230503123359661?f=o",
                "written_at": date(2023, 5, 3),
            },
            {
                "title": "중앙선 넘어 돌진한 빨간 페라리... 가만히 있던 닛산 붕 떴다",
                "content": "호주의 한 도로에서 페라리 차가 중앙 선을 침범하며 돌진하는 바람에 닛산 차가 공중에 붕 뜨는 사고가 발생했다.2일(현지 시각) 7뉴스와 데일리메일 등에 따르면 지 난 30일 오후 4시30분쯤 호주 멜버른 교외의 한 도로에서 빨간색 페라리가 닛산 SUV 차에 정면충돌했다. 당시는 멜번크리켓구장 에서 호주풋볼리그(AFL)가 끝난 직후였기 때문에 경기 관람 후 귀가하는 관객들로 교통 체증이 심한 상황이었다.당시 상황이 담 긴 블랙박스 영상이 소셜미디어를 통해 확산하기도 했다. 영상을 보면, 빨간색 페라리 한 대가 돌연 중앙선을 넘어 돌진하더니, 신호 대기 중이던 닛산 차를 박는다. 닛산 차는 충격에 의해 공중으로 붕 떠올랐다가 옆의 검은색 차 위로 털썩 내려앉는다.충격 여파로 페라리는 전면 보닛이 형체를 알아보기 힘들 정도로 일그러졌다. 정작 페라리에 의해 공중으로 떠오른 닛산 차는 앞 창 문에 약간의 금이 간 것을 제외하고는 외관상 큰 문제는 발생하지 않았다. 다만 닛산 옆에 서 있던 검은색 차 앞 범퍼가 모두 떨어져 나가는 등의 피해를 봤다.닛산 운전자는 “교통 체증에 가만히 앉아 있었는데 갑자기 페라리가 돌진하는 소리가 들렸고, 그 이후 차가 들어 올려져 다른 차 위로 떨어졌다”며 “즉시 뛰쳐나와 밑에 깔린 차로 달려가 운전자를 구했다”고 했다.호주 페 라리 클럽의 제프 페더브리지 총무는 사고 차 모델이 2004년형 페라리 360 챌린지 스트라달레로, 가격이 60만달러(약 8억원)에  달한다고 설명했다. 다만 차를 수리하기는 어려울 것이라고 했다. 사고 페라리 엔진이 특별 제작된 모델이라서 부품을 구하기 힘들다는 이유에서다. 제프는 “해당 모델에 대한 예비 부품은 어디에도 없을 것”이라고 했다.경찰에 따르면 이번 사고로 크게 다친 사람은 없다. 현재까지 페라리 차주의 음주 및 마약 여부 등은 공개되지 않았다. 경찰 관계자는 아직 자세한 사고 경위를 조 사하고 있다며 “관련 차 운전을 목격했거나 사건에 대한 블랙박스 또는 기타 비디오 영상을 가지고 있는 사람은 제보해달라”고 했다.",
                "url": "https://v.daum.net/v/20230503190100002?f=o",
                "written_at": date(2023, 5, 3),
            },{
            'title': '‘작전명 스펙터’ 9國 연합 마약전쟁... 850㎏·700억원 압수했다',
            'content': '3개 대륙, 9개국, 29개 기관의 정예 수사 인력들이 참여한 사상 최대규모의 국제 마약범죄 퇴치작전인 스펙터 작전(Operation SpecTor)이 전세계에서 288명의 마약사범을 검거하고 850㎏의 마약과 700억원 넘는 검은돈을 압수하는 성과를 거뒀다. 무장한 마약사범 등이 갖고 있던 총기 117정도 확보했다. 마약사범들의 수법이 갈수록 지능화되고 마약이 걷잡을 수 없이 확산하면서 이와 같은 국제 공조 퇴치작전이 앞으로도 전개될 것이라는 전망이 나온다.미 연방법무부와 연방수사국(FBI), 유로폴 등 참여 기관들이 2일(현지 시각) 이번 작전 성과를 발표했다. 우선 이번 작전을 통해 다크넷을 활용해 마약 밀매와 공급에 연루된 혐의를 받는 288명을 체포해 신병을 확보했다. 이 중 53%(153명)가 미국에서 붙잡혔으며 영국(55명), 독일(52명), 네덜란드(10명)순으로 체포된 용의자 숫자가 많았다. 다크넷이란 표준 프로토콜과 포트를 사용하지 않고 IP 주소도 공유않는 익명의 인터넷 공간으로 일반적으로 마약과 인신매매 등 강력범죄에 활용된다. 암페타민 258㎏, 코카인과 MDMA 각 43㎏, LSD와 엑스터시 알약 각 10㎏ 등을 포함한 850㎏의 마약도 몰수했다. 무장한 마약조직원들로부터 총기 117정을 확보한 것도 성과로 꼽힌다. 마약 거래에 연루된 ‘검은돈’ 역시 현금과 가상화폐를 합쳐 5340만 달러(약 714억원)에 달한다.미 법무부는 이번 작전에 대해 “지금까지 실행됐던 마약관련 국제공조 수사 중엔서 가장 큰 규모로 펼쳐졌다”고 밝혔다. 앞서 지난 2021년에도 FBI와 유로폴 등이 협업해 10개월동안 진행한 공조수사를 통해 거둔 성과(150여명 체포·마약 234㎏ 압수)를 뛰어넘는 규모다. 미국은 최근 마약성 진통제 오피오이드 오·남용 문제로 사망자가 급증하면서 다크넷 등을 이용한 국제 마약 거래망을 분쇄하기 위한 해외 공조 수사에 주력해왔다. 이번 ‘스펙터 작전’은 다국적 수사기관이 협업한 다섯번째 작전이다. 이번 작전에는 연방 법무부·국방부·FBI·DEA(마약수사국)·ICE(이민세관국)·FDA(식품의약국)·해군범죄수사국(NCIS) 등 12개 수사기관이 참가했다.해외에서도 유로폴을 비롯해 국립범죄수사국(영국)· 연방수사청(오스트리아)·프랑크푸르트 연방검찰과 베를린 경찰(독일)·국립경찰(네덜란드)·중앙범죄수사국(폴란드)·연방경찰(브라질) 등도 참여했다. 체포된 용의자에 대한 수사와 기소가 속속 진행되면서 중형 선고가 내려지는 사례도 나왔다. 2021년 5월부터 2022년 5월 사이에 다크넷을 통해 가상화폐로 펜타닐·메스암페타민·헤로인 등 마약을 확보한 뒤 우편물로 미국 전역에 공급하려다 적발된 플로리다 출신 마약사범 3명 중 2명에게 지난해 12월 각각 징역 16년과 징역 11년이 선고됐으며, 나머지 한 명은 곧 선고를 앞두고 있다. 이들과 거래하는 고객 명단은 미국 전역에 6000여명에 달한 것으로 알려졌다.미국에서 마약 범죄는 국가 기강을 송두리째 흔드는 최대의 위협으로 떠올랐다. 오피오이드 중독 관련 사망자는 2020년 5만7834명에서 2021년 7만1238명에서 1년새 15% 늘어날 정도로 폭증세다. 이에 따라 각국이 협업하는 ‘글로벌 마약과의 전쟁’도 더욱 큰 규모로 전개될 것이라는 전망이 나온다. 이번 작전에 참가한 기관 책임자와 담당자들도 모두 국제 공조 수사의 필요성을 강조했다.캐서린 드 볼 유로폴 국장은 “세 대륙에 걸친 사법기관들이 공조한 이번 작전은함께 할 때 더 나은 성과를 보여준다는 것을 보여줬다”며 “국제사법공조는 다크넷을 통한 범죄자들에게도 책임을 물을 수 있는 수단이 있다”고 말했다. 크리스토퍼 레이 FBI 국장은 “이번 작전은 왜 우리가 문제 해결을 위해 해외 파트너들과 협력해야 하는지를 보여줬다”고 했다. 메릭 갈런드 미국 법무부장관(연방 검찰총장)은 “이번 공조 작전이 범죄집단에 주는 메시지는 명확하다”며 “인터넷에 접속해 최대한 검은돈을 꽁꽁 숨기려 해도 우리는 찾아내 책임을 물을 것이라는 것”이라고 했다.',
            'written_at': date(2023, 5, 3),
            'url': 'https://v.daum.net/v/20230503144403510?f=o'
            },
        ]
        self.articles_kbs_data = [
            # kbs
            {
            'title': 'SNS로 마약 거래, 외국인 무더기 검거',
            'content': '[앵커]\n\n남해안 일대에서 마약을 투약하거나 공급한 외국인 15명이 무더기로 경찰에 붙잡혔습니다.\n\n이들은 현지인들이 주로 쓰는 SNS를 통해 마약을 거래했고, 본국을 오가는 사람을 활용해 마약을 국내로 반입했습니다.\n\n보도에 김민지 기자입니다.\n\n[리포트]\n\n해경 경비함정이 바지선 옆 소형 선박에 다가가고 선별 작업을 하던 외국인 노동자를 체포합니다.\n\n동전 빨래방에 들이닥친 경찰은 저항하던 외국인을 붙잡습니다.\n\n차량 4대가 도로 위에 서 있던 승용차 한 대를 에워쌉니다.\n\n["다리, 다리, 잡아."]\n\n경찰차를 추돌한 뒤 도주하려던 남성을 붙잡기 위해 도로에서 몸싸움이 벌어집니다.\n\n통영해경이 마약류인 엑스터시와 케타민 등을 복용하거나 공급한 혐의로 외국인 15명을 붙잡았습니다.\n\n유통 총책 2명과 중간 판매책 등 5명은 구속 송치됐습니다.\n\n이들은 주로 우편이나 본국을 오가는 사람들을 이른바 \'지게꾼\'으로 이용해 국내로 마약을 들여왔습니다.\n\n대구에서 활동하는 상위 유통책을 통해 김해·부산의 중간 판매책에게 마약을 공급하면 중간 판매책들은 거제 지역 하위 판매책들에게 공급하는 방식이었습니다.\n\n외국인들은 주로 노래주점이나 외국인 전용 클럽 등에서 마약을 투약했습니다.\n\n[이정석/통영해양경찰서 수사과장 : "일하면서 힘든 노동과 고향에 대한 향수, 이런 것들 때문에 자기 나라 사람들끼리 모여서 마약을 투약했다고 (진술하고 있습니다)."]\n\n거래 대금은 현금 던지기 수법이 활용됐습니다.\n\n텔레그램 외에도 현지인들이 주로 쓰는 SNS를 통해 마약을 거래했고, 경찰은 상위 유통책의 SNS 아이디를 확보해 일당을 검거할 수 있었습니다.\n\n해경은 조선소와 양식장이 밀집한 남해안 일대를 중심으로 외국인 마약 유통조직이 더 있을 것으로 보고 수사를 확대하고 있습니다.\n\nKBS 뉴스 김민지입니다.\n\n촬영기자:최현진',
            'written_at': date(2023, 5, 3),
            'url': 'https://v.daum.net/v/20230503065139459?f=o'
            },
        ]
        self.articles_yeonhap_data = [
            # yeonhap
            {
            'title': "'마약음료' 일당 구속기소…'최대 사형' 혐의 적용",
            'content': '[연합뉴스 자료사진](서울=연합뉴스) 박형빈 기자 = 검찰이 강남 학원가 \'마약 음료\'를 제조·공급한 보이스피싱 조직원 일당 3명을 재판에 넘겼다.검찰은 특히 최고 사형까지 구형할 수 있는 마약류관리법상 \'영리목적 미성년자 마약 투약\' 혐의를 적용했다.서울중앙지검 전담수사팀(신준호 부장검사)은 4일 마약류관리법 위반 및 범죄단체가입·활동 등 혐의로 마약 음료 제조·공급자 길모 씨와 보이스피싱 전화중계기 관리책 박모 씨를 구속기소 했다.별건의 마약 판매 혐의로 이미 구속기소 된 전달책 박모 씨는 길씨에게 마약을 전달한 혐의로 추가 기소됐다.이들은 중국 소재 보이스피싱 조직과 공모해 마약 음료를 제조, \'집중력 강화 음료 무료 시음회\'를 빙자해 강남 학원가에서 제공한 것으로 드러났다.길씨는 지정된 장소에 마약을 가져다 두는 이른바 \'던지기 수법\'으로 박씨로부터 얻은 필로폰 10g을 우유와 섞어 직접 마약 음료 100병을 제조, 미성년자 13명에게 준 혐의를 받는다.이 가운데 9명이 실제로 마약 음료를 마셨고, 그 가운데 6명은 환각 등 증상을 겪은 것으로 검찰은 파악했다.애초 경찰은 법정 최고형이 무기징역인 \'미성년자 마약제공\' 혐의로 길씨를 송치했지만, 검찰은 한층 중한 \'영리목적 미성년자 마약투약\' 혐의를 적용했다.마약류 관리에 관한 법률은 영리를 목적으로 미성년자에게 마약을 상습적으로 수수·조제·투약·제공한 자에게는 사형·무기징역 또는 10년 이상의 징역에 처하도록 한다.아울러 검찰은 마약 음료를 복용한 피해자들이 환각 증세를 보인 것에 대해서는 길씨에게 특수상해 혐의를 적용했다.피해자의 부모 6명에게 \'자녀를 마약 투약 혐의로 신고하겠다\'고 협박해 금품을 요구한 혐의(공갈미수)도 있다.김씨는 일당이 피해 학부모에게 협박 전화를 거는 과정에서 중계기를 이용해 070으로 시작하는 중국 인터넷전화 번호를 국내 휴대전화 번호(010)로 변작해준 혐의를 받는다. 차명 계좌로 범죄 수익 1천542만원을 입금받아 자금을 세탁한 혐의도 있다.검찰은 사건 송치 이후 길씨 등과 통화한 300여명의 대한 계좌거래·출입국 내역 등을 분석해 추가로 보이스피싱 조직원 모집책 이모씨를 국내에서 검거, 이달 2일 체포해 구속영장을 청구했다.이씨의 구속 전 피의자 심문(영장심사)은 5일 오후 서울중앙지법 이용제 판사 심리로 열릴 예정이다.검찰은 중국 공안 등과 공조해 보이스피싱 총책을 비롯한 국내·외 추가 공범에 대한 수사에 나선다는 방침이다.검찰은 "불특정 청소년을 속여 마약 음료를 투약하고 갈취 수단으로 활용한 신종 보이스피싱 범죄"라며 "죄질에 상응하는 처벌이 이뤄지도록 철저하게 공소를 유지하고, 범죄수익을 끝까지 추적해 환수하겠다"고 밝혔다.', 
            'written_at': date(2023, 5, 4),
            'url': 'https://v.daum.net/v/20230504113522195?f=o'
            }
        ]
        Article.objects.bulk_create(
            [Article(**article_data) for article_data in self.articles_chosun_data+self.articles_kbs_data+self.articles_yeonhap_data]
        )

    def test_save_articles(self):
        with patch("apps.data_collection.crawler.article_crawler.ArticleCrawler.get_article_links") as mock_get_article_links:
            mock_get_article_links.return_value = {
                "chosun": ['https://v.daum.net/v/20230503123359661?f=o', 'https://v.daum.net/v/20230503190100002?f=o', 'https://v.daum.net/v/20230503144403510?f=o'],
                "kbs" : ['https://v.daum.net/v/20230503065139459?f=o'],
                "yeonhap" : ['https://v.daum.net/v/20230504113522195?f=o'],
            }
            with patch("apps.data_collection.crawler.chosun_article_crawler.ChosunArticleCrawler.get_articles") as mock_get_chosun_articles:
                with patch("apps.data_collection.crawler.kbs_article_crawler.KbsArticleCrawler.get_articles") as mock_get_kbs_articles:
                    with patch("apps.data_collection.crawler.yeonhap_article_crawler.YeonhapArticleCrawler.get_articles") as mock_get_yeonhap_articles:
                        mock_get_chosun_articles.return_value = self.articles_chosun_data
                        mock_get_kbs_articles.return_value = self.articles_kbs_data
                        mock_get_yeonhap_articles.return_value = self.articles_yeonhap_data
                        
                        save_articles()
                        filter_date = datetime.strptime("2023.05.03", '%Y.%m.%d').date()
                        saved_articles = Article.objects.filter(written_at=filter_date)
                        self.assertEqual(saved_articles.count(), 8)

    def test_parse_article_to_word(self):
        articles = Article.objects.all()
        with patch("apps.data_collection.views.save_word") as mock_save_word:
            for article in articles:
                mock_save_word.reset_mock()  # reset the mock for each article
                parse_article_to_word()
                mock_calls = mock_save_word.mock_calls
                kkma = Kkma()
                words = kkma.nouns(article.content)

                for word in words:
                    call_args_list = [call[1] for call in mock_calls]
                    assert any( call_args[0] == article and call_args[1] == word for call_args in call_args_list)


class SaveWordTestCase(TestCase):
    def test_save_word(self):
        article = Article.objects.create( 
            title =  "케타민 20만명분 밀수한 마약 조직 운반책 2명 구속기소",
            content ="‘클럽 마약’으로 불리는 케타민 20만명 투 약분을 밀수한 마약 조직원 2명이 재판에 넘겨졌다. 올해 초부터 시작된 관련 수사로 검찰이 적발한 조직원은 10명이 넘는다.3일 검찰에 따르면, 서울중앙지검 강력범죄수사부는 케타민 밀수 조직 운반책으로 활동한 20대 A씨 등 2명을 특정범죄가중법과 범죄단체 가입 등 혐의로 최근 구속기소했다.일당은 조직 차원에서 현지 태국 마약상과 접촉해 대량으로 사들인 케타민을 각각 5.4㎏과 1.8㎏씩 인천국제공항을 통해 몰래 들여온 것으로 조사됐다. A씨 등 운반책들은 비닐랩으로 감싼 케타민을 속옷 안에 숨기는 방식으로 밀수한 것으로 조사됐다.작년 말 케타민 밀수조직 범죄첩보를 입수해 수사해 온 검찰은 최근까지 이 사건과 관련해 현 재까지 총 15명을 검거했다. 검찰은 검거한 조직원들 대부분이 밀수에 가담한 것으로 보고, 판매책 검거에 수사력을 집중하고 있는 것으로 전해졌다.케타민은 의료용 또는 동물용 마취제의 일종으로, 젊은 층 사이에서 ‘클럽 마약’으로 불린다. 케타민은 필로폰이나 코카인보다 싸게 구입할 수 있고 술이나 음료에 타서 마실 수 있다. 다른 사람 음료에도 몰래 타기 쉬워 피해 발생 우 려가 큰 마약이다.",
            url = "https://v.daum.net/v/20230503123359661?f=o",
            written_at = datetime.strptime("2023.05.03", '%Y.%m.%d').date()
        )
        text = "케타민"

        saved_word = save_word(article, text)

        self.assertIsInstance(saved_word, Word)
        self.assertEqual(saved_word.article_id, article)
        self.assertEqual(saved_word.text, text)
        self.assertEqual(saved_word.frequency, 1)

        # test saving an existing word
        saved_word = save_word(article, text)

        self.assertIsInstance(saved_word, Word)
        self.assertEqual(saved_word.article_id, article)
        self.assertEqual(saved_word.text, text)
        self.assertEqual(saved_word.frequency, 2)

        # test invalid article id
        with self.assertRaises(ValueError):
            save_word(article.article_id + 1, text)

        # test invalid text
        with self.assertRaises(ValueError):
            save_word(article, None)