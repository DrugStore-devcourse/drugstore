import time
import logging
from typing import List
from datetime import datetime
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException, WebDriverException
from apps.data_collection.crawler.chrome_driver import ChromeDriver


class ChosunArticleCrawler : 


    def __init__(self):
        self.logger = logging.getLogger('crawlerlogger')
        self.driver = ChromeDriver()

    def get_articles(self, links: List[str]) -> List[dict]:
        '''
        This function gets aritlce contents of 'chosun' press. 
        
        :param links: List[str] - List of links to ChosunIlbo(=chosun) articles
        '''
        article_list = []
        try: 
            self.driver.start()
            for link in links:
                self.driver.get_driver().get(link)
                time.sleep(0.5)

                title = self.driver.get_driver().find_element(by=By.CSS_SELECTOR, value="#fusion-app > div.article.\| > div:nth-child(2) > div > div > div.article-header__headline-container.\|.box--pad-left-md.box--pad-right-md > h1 > span").text
                written_at = self.driver.get_driver().find_element(by=By.XPATH, value='//*[@id="fusion-app"]/div[1]/div[2]/div/section/article/div[2]/span')
                written_at = written_at.text.split()[1][:-1]
                written_at_obj = datetime.strptime(written_at, '%Y.%m.%d').date()
                total_contents = ''
                contents = self.driver.get_driver().find_elements(by=By.CSS_SELECTOR, value="#fusion-app > div.article.\| > div:nth-child(2) > div > section > article > section > p")
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
            self.logger.warning(f'Failed to get Chosun article: {str(e)}')
        finally:
            self.driver.stop()

        return article_list