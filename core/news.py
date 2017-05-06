from requests import get
from bs4 import BeautifulSoup as BS
import re

def get_index_news():
    news_list = []
    page = BS(get('http://store.steampowered.com/news/').text, 'html.parser')
    news = page.find_all('div', id=re.compile(r'post_\d+'))
    for n in news:
        title = n.find('div', 'posttitle').a.string
        news_link = n.find('div', 'posttitle').a['href']
        news_id = re.compile(r"\d+").search(news_link)
        
        author = n.find('div', 'feed').string
        date = n.find('div', 'date').string
        body = n.find('div','body').get_text()

        has_game = n.find('div','body').find('a', href=re.compile(r'http://store.steampowered.com/app/\d+/'))
        if has_game:    
            game_link = has_game['href']
            game_id = re.compile(r'\d+').search(game_link)
        
        has_titleimg = n.find('img', 'capsule')
        if has_titleimg:
            title_img = has_titleimg['src']

        n_info = {
            'title': title,
            'news_link': news_link,
            'author': author,
            'date': date,
            'body': body,
            'game_link': game_link,
            'title_img': title_img
        }
        news_list.append(n_info)
    return news_list

if __name__ == '__main__':
    get_index_news()