import time
import logging
from typing import List
from datetime import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException, WebDriverException
from apps.data_collection.crawler.chrome_driver import ChromeDriver


class YeonhapArticleCrawler : 


    def __init__(self):
        self.logger = logging.getLogger('crawlerlogger')
        self.driver = ChromeDriver()

    def get_articles(self, links: List[str]) -> List[dict]:
        '''
        This function gets aritlce contents of 'yeonhap' press. 
        
        :param links: List[str] - List of links to YeonhapNews(=yeonhap) articles
        '''
        article_list = []
        try: 
            self.driver.start()
            for link in links:
                self.driver.get_driver().get(link)
                time.sleep(0.8)
                page_type = self.driver.get_driver().find_element(by=By.TAG_NAME, value="body").get_attribute('class')
                title = self.driver.get_driver().find_element(by=By.TAG_NAME, value="h1").text
                total_contents = ''
                if "page-photo" in page_type or "graphic" in page_type: 
                    written_at = WebDriverWait(self.driver.get_driver(), 15).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '#viewWrap > div.inner-article > p > span')))   
                    written_at_obj = datetime.strptime(written_at[0].text.split(" ")[0] , '%Y/%m/%d').date()
                    contents = self.driver.get_driver().find_element(by=By.CSS_SELECTOR, value="#viewWrap > div.inner-article > div.article-txt").find_elements(by=By.TAG_NAME, value="p")
                else :
                    written_at = self.driver.get_driver().find_element(by=By.CSS_SELECTOR, value='#newsUpdateTime01').get_attribute("data-published-time")[:8]
                    written_at_obj = datetime.strptime(written_at, '%Y%m%d').date()
                    contents = self.driver.get_driver().find_element(by=By.CSS_SELECTOR, value="#articleWrap > div.content01.scroll-article-zone01 > div > div > article").find_elements(by=By.TAG_NAME, value="p")
                
                for content in contents:
                    total_contents += content.text
                    
                article = {
                    'title' : title,
                    'content' : total_contents,
                    'written_at' : written_at_obj,
                    'url' : link,
                }
                article_list.append(article)
        except NoSuchElementException as e:
            self.logger.warning(f'Failed to find element: {str(e)}')
        except TimeoutException as e:
            self.logger.warning(f'Page load timed out: {str(e)}')
        except WebDriverException as e:
            self.logger.warning(f'Failed to get Yeonhap article: {str(e)}')
        finally:
            self.driver.stop()

        return article_list