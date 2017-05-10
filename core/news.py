#coding: utf-8
from requests import get
from bs4 import BeautifulSoup as BS
import re

class SteamNews(object):
    """docstring for SteamNews"""
    def __init__(self):
        super(SteamNews, self).__init__()
        # self.arg = arg
        self.index_page = BS(get('http://store.steampowered.com/news/').text, 'html.parser')
        self.cur_page = self.index_page

        
    def get_news(self, page_soup):
        # 每次加载的页面能取10条
        news_list = []
        news = page_soup.find_all('div', id=re.compile(r'post_\d+'))
        for n in news:
            title = n.find('div', 'posttitle').a.string
            news_link = n.find('div', 'posttitle').a['href']
            news_id = re.compile(r"\d+").search(news_link)
            
            author = n.find('div', 'feed').string
            date = n.find('div', 'date').string
            body = n.find('div','body').get_text()

            # 每条都会有的信息
            n_info = {
                'title': title,
                'news_link': news_link,
                'author': author,
                'date': date,
                'body': body,
            }

            # 可能会有的信息
            has_game = n.find('div','body').find('a', href=re.compile(r'http://store.steampowered.com/app/\d+/'))
            if has_game:    
                game_link = has_game['href']
                game_id = re.compile(r'\d+').search(game_link).group(0)
                n_info['game_link'] = game_link
                n_info['game_id'] = game_id
            
            has_titleimg = n.find('img', 'capsule')
            if has_titleimg:
                title_img = has_titleimg['src']
                n_info['title_img'] = title_img

            news_list.append(n_info)
        self.get_next_page(page_soup) # 加载下一个页面
        return news_list

    def get_next_page(self, page_soup):
        last_news = page_soup.find_all('div', id=re.compile(r'post_\d+'))[-1]
        # print last_news
        last_news_id = re.compile(r't=(\d+)').search(last_news.find('img', 'capsule')['src']).group(1)
        self.cur_page = BS(get('http://store.steampowered.com/news/posts/?enddate=%s' % last_news_id).text, 'html.parser')

    def get_index_news(self):
        ''' 获取首页新闻 '''
        return self.get_news(self.index_page)

    def get_some_news(self, count=10, enddate=0):
        # 获取特定条数的新闻
        # enddate是上一条新闻的标题图结尾的一串数字
        if int(enddate) == 0:
            start_page = self.index_page
        else:
            start_page = BS(get('http://store.steampowered.com/news/posts/?enddate=%s' % enddate).text, 'html.parser')

        news_list = []
        count = int(count)
        if count > 10:
            news_list = self.get_news(start_page)
            while count > 10:
                count = count - 10
                news_list += self.get_news(self.cur_page)[:count]
        else:
            news_list = self.get_news(start_page)[:count]
        
        return news_list               

if __name__ == '__main__':
    news = SteamNews()
    for i in news.get_some_news('15', '1494302425'):
        print i['title'] + '\t' + i['author'] + '\t' + i['date'] + '\n'