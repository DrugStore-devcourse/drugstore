import logging
import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta


class ArticleCrawler : 


    def __init__(self):
        self.logger = logging.getLogger('crawlerlogger')

    def get_article_links(self, presses:dict) -> dict: 
        '''
        This function gets links to drug-related news articles from each press from the previous day.

        :param presses: dict - Dictionary of 'press' keys and lists of article links values
        '''
        article_links = {}

        for press in presses : 
            article_links[press] = []
            today = datetime.today().strftime('%Y%m%d') + "000000"
            yesterday = (datetime.today() - timedelta(days=1)).strftime('%Y%m%d') + "000000"
            presses[press] = presses[press].replace('{{startdate}}', yesterday)
            presses[press] = presses[press].replace('{{enddate}}', today)
            try:
                res = requests.get(presses[press])
                soup = BeautifulSoup(res.text, "html.parser")

                # Count pages
                num_aritcle = int(soup.find("div" , "sub_expander").span.text.split('/ ')[1].split("건")[0])
                if num_aritcle > 1 :
                    pages = (num_aritcle - 1)  // 10 
                else : 
                    pages = 0
                pages += 1

                # Get article links per page
                for p in range(1, pages+1) : 
                    res = requests.get(presses[press] + "&p=" + str(p))
                    soup = BeautifulSoup(res.text, "html.parser")
                    list_articles = soup.find("ul" , "list_news")
                    if list_articles:
                        articles = list_articles.find_all("li")
                        for article in articles: 
                            link = article.find("a").get('href')
                            article_links[press].append(link)
            except requests.exceptions.RequestException as e:
                    self.logger.error(f'Error occurred while getting article links from {press}: {str(e)}')
                    continue
        return article_links