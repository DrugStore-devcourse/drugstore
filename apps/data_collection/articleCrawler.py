from bs4 import BeautifulSoup
import requests
from datetime import datetime, timedelta
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import logging
import time


class ArticleCrawler : 
    def __init__(self):
        self.logger = logging.getLogger('crawlerlogger')
        self.driver = self.create_chromedriver()


    def create_chromedriver(self) :
        user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299"
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option('excludeSwitches', ["enable-logging"])
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--disable-extensions')
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('user-agent=' + user_agent)

        try:
            driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
        except WebDriverException as e:
            self.logger.error(f"Error while creating chromedriver: {e}")
            driver = None
        except Exception as e:
            self.logger.error(f"Error while creating chromedriver: {e}")
            driver = None
        
        self.logger.info("Complete to create chromedriver")
        return driver


    def get_article_links(self, presses:dict) -> dict: 
        '''
        This function gets links to drug-related news articles from each press from the previous day.

        <<TODO>> try-exception, logging
        '''
        article_links = {}

        for press in presses : 
            article_links[press] = []
            today = datetime.today().strftime('%Y%m%d') + "000000"
            yesterday = (datetime.today() - timedelta(days=1)).strftime('%Y%m%d') + "000000"
            presses[press] = presses[press].replace('{{startdate}}', yesterday)
            presses[press] = presses[press].replace('{{enddate}}', today)
            res = requests.get(presses[press])
            soup = BeautifulSoup(res.text, "html.parser")

            # 페이지 계산 
            num_aritcle = int(soup.find("div" , "sub_expander").span.text.split('/ ')[1].split("건")[0])
            if num_aritcle > 1 :
                pages = (num_aritcle - 1)  // 10 
            else : 
                pages = 0
            pages += 1

            # 페이지 별 링크 가져옴
            for p in range(1, pages+1) : 
                res = requests.get(presses[press] + "&p=" + str(p))
                soup = BeautifulSoup(res.text, "html.parser")
                articles = soup.find("ul" , "list_news").find_all("li")
                for article in articles: 
                    link = article.find("a").get('href')
                    article_links[press].append(link)
        return article_links


    def get_chosun_article(self, link:str) -> dict:
        '''
        This function gets aritlce contents of 'chosun' press. 
        <<TODO>> try-exception, logging
        '''
        self.driver.get(link)
        time.sleep(0.5)

        title = self.driver.find_element(by=By.CSS_SELECTOR, value="#fusion-app > div.article.\| > div:nth-child(2) > div > div > div.article-header__headline-container.\|.box--pad-left-md.box--pad-right-md > h1 > span").text
        written_at = self.driver.find_element(by=By.XPATH, value='//*[@id="fusion-app"]/div[1]/div[2]/div/section/article/div[2]/span')
        written_at = written_at.text.split()[1][:-1]
        written_at_obj = datetime.strptime(written_at, '%Y.%m.%d').date()
        total_contents = ''
        contents = self.driver.find_elements(by=By.CSS_SELECTOR, value="#fusion-app > div.article.\| > div:nth-child(2) > div > section > article > section > p")
        for content in contents:
            total_contents += content.text

        article = {
            'title' : title,
            'content' : total_contents,
            'written_at' : written_at_obj,
            'url' : link,
        }

        return article



    def main(self) -> dict:
        presses = {
        'chosun' : 'https://search.daum.net/search?w=news&q=%EB%A7%88%EC%95%BD&DA=STC&spacing=0&period=d&sd={{startdate}}&ed={{enddate}}&cp=16d4PV266g2j-N3GYq&cpname=%EC%A1%B0%EC%84%A0%EC%9D%BC%EB%B3%B4',
        'yeonhap' : 'https://search.daum.net/search?w=news&q=%EB%A7%88%EC%95%BD&DA=STC&spacing=0&period=d&sd={{startdate}}&ed={{enddate}}&cp=16X5Xh1MWS7Qt1sMrW&cpname=%EC%97%B0%ED%95%A9%EB%89%B4%EC%8A%A4',
        'kbs' : 'https://search.daum.net/search?nil_suggest=btn&w=news&DA=STC&cluster=y&q=%EB%A7%88%EC%95%BD&period=d&sd={{startdate}}&ed={{enddate}}&cp=16hWxJmTql2y9rxiuO&cpname=kbs'
        }

        article_links = self.get_article_links(presses)

        for link in article_links['chosun'] : 
            self.get_chosun_article(link)