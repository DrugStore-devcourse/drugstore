from konlpy.tag import Kkma
from datetime import datetime
from django.test import TestCase
from unittest.mock import patch, call
from apps.data_collection.models import Article, Word
from apps.data_collection.views import save_articles, parse_article_to_word, save_word

class ArticleTestCase(TestCase):
    def setUp(self):
        self.articles_data = [
            {
                "title": "케타민 20만명분 밀수한 마약 조직 운반책 2명 구속기소",
                "content": "‘클럽 마약’으로 불리는 케타민 20만명 투 약분을 밀수한 마약 조직원 2명이 재판에 넘겨졌다. 올해 초부터 시작된 관련 수사로 검찰이 적발한 조직원은 10명이 넘는다.3일 검찰에 따르면, 서울중앙지검 강력범죄수사부는 케타민 밀수 조직 운반책으로 활동한 20대 A씨 등 2명을 특정범죄가중법과 범죄단체 가입 등 혐의로 최근 구속기소했다.일당은 조직 차원에서 현지 태국 마약상과 접촉해 대량으로 사들인 케타민을 각각 5.4㎏과 1.8㎏씩 인천국제공항을 통해 몰래 들여온 것으로 조사됐다. A씨 등 운반책들은 비닐랩으로 감싼 케타민을 속옷 안에 숨기는 방식으로 밀수한 것으로 조사됐다.작년 말 케타민 밀수조직 범죄첩보를 입수해 수사해 온 검찰은 최근까지 이 사건과 관련해 현 재까지 총 15명을 검거했다. 검찰은 검거한 조직원들 대부분이 밀수에 가담한 것으로 보고, 판매책 검거에 수사력을 집중하고 있는 것으로 전해졌다.케타민은 의료용 또는 동물용 마취제의 일종으로, 젊은 층 사이에서 ‘클럽 마약’으로 불린다. 케타민은 필로폰이나 코카인보다 싸게 구입할 수 있고 술이나 음료에 타서 마실 수 있다. 다른 사람 음료에도 몰래 타기 쉬워 피해 발생 우 려가 큰 마약이다.",
                "url": "https://v.daum.net/v/20230503123359661?f=o",
                "written_at": datetime.strptime("2023.05.03", '%Y.%m.%d').date()
            },
            {
                "title": "중앙선 넘어 돌진한 빨간 페라리... 가만히 있던 닛산 붕 떴다",
                "content": "호주의 한 도로에서 페라리 차가 중앙 선을 침범하며 돌진하는 바람에 닛산 차가 공중에 붕 뜨는 사고가 발생했다.2일(현지 시각) 7뉴스와 데일리메일 등에 따르면 지 난 30일 오후 4시30분쯤 호주 멜버른 교외의 한 도로에서 빨간색 페라리가 닛산 SUV 차에 정면충돌했다. 당시는 멜번크리켓구장 에서 호주풋볼리그(AFL)가 끝난 직후였기 때문에 경기 관람 후 귀가하는 관객들로 교통 체증이 심한 상황이었다.당시 상황이 담 긴 블랙박스 영상이 소셜미디어를 통해 확산하기도 했다. 영상을 보면, 빨간색 페라리 한 대가 돌연 중앙선을 넘어 돌진하더니, 신호 대기 중이던 닛산 차를 박는다. 닛산 차는 충격에 의해 공중으로 붕 떠올랐다가 옆의 검은색 차 위로 털썩 내려앉는다.충격 여파로 페라리는 전면 보닛이 형체를 알아보기 힘들 정도로 일그러졌다. 정작 페라리에 의해 공중으로 떠오른 닛산 차는 앞 창 문에 약간의 금이 간 것을 제외하고는 외관상 큰 문제는 발생하지 않았다. 다만 닛산 옆에 서 있던 검은색 차 앞 범퍼가 모두 떨어져 나가는 등의 피해를 봤다.닛산 운전자는 “교통 체증에 가만히 앉아 있었는데 갑자기 페라리가 돌진하는 소리가 들렸고, 그 이후 차가 들어 올려져 다른 차 위로 떨어졌다”며 “즉시 뛰쳐나와 밑에 깔린 차로 달려가 운전자를 구했다”고 했다.호주 페 라리 클럽의 제프 페더브리지 총무는 사고 차 모델이 2004년형 페라리 360 챌린지 스트라달레로, 가격이 60만달러(약 8억원)에  달한다고 설명했다. 다만 차를 수리하기는 어려울 것이라고 했다. 사고 페라리 엔진이 특별 제작된 모델이라서 부품을 구하기 힘들다는 이유에서다. 제프는 “해당 모델에 대한 예비 부품은 어디에도 없을 것”이라고 했다.경찰에 따르면 이번 사고로 크게 다친 사람은 없다. 현재까지 페라리 차주의 음주 및 마약 여부 등은 공개되지 않았다. 경찰 관계자는 아직 자세한 사고 경위를 조 사하고 있다며 “관련 차 운전을 목격했거나 사건에 대한 블랙박스 또는 기타 비디오 영상을 가지고 있는 사람은 제보해달라”고 했다.",
                "url": "https://v.daum.net/v/20230503190100002?f=o",
                "written_at": datetime.strptime("2023.05.03", '%Y.%m.%d').date()
            }
        ]
        Article.objects.bulk_create(
            [Article(**article_data) for article_data in self.articles_data]
        )

    def test_save_articles(self):
        with patch("apps.data_collection.crawler.article_crawler.ArticleCrawler.get_article_links") as mock_get_article_links:
            mock_get_article_links.return_value = {"chosun": ["https://v.daum.net/v/20230503123359661?f=o", "https://v.daum.net/v/20230503190100002?f=o"]}

            with patch("apps.data_collection.crawler.chosun_article_crawler.ChosunArticleCrawler.get_articles") as mock_get_articles:
                mock_get_articles.return_value = self.articles_data

                save_articles()

                filter_date = datetime.strptime("2023.05.03", '%Y.%m.%d').date()
                saved_articles = Article.objects.filter(written_at=filter_date)
                self.assertEqual(saved_articles.count(), 4)

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

'''
테스트 실행 명령어 :
manage.py test apps.data_collection.tests.test_views.ArticleTestCase
manage.py test apps.data_collection.tests.test_views.SaveWordTestCase
'''