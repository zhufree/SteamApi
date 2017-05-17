#coding: utf-8
from requests import get
from bs4 import BeautifulSoup as BS
import re

class SteamItem(object):
    """docstring for SteamItem"""
    def __init__(self):
        super(SteamItem, self).__init__()
        # self.arg = arg
        self._headers = {
            'Host': 'steamdb.info',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
            'Accept-Encoding': 'gzip, deflate',
            'Referer': 'http://www.baidu.com',
            'Connection': 'keep-alive',
            'Cache-Control': 'max-age=0',
        }

    def get_app_info(self, appid):
        app_page = BS(get('https://steamdb.info/app/%s/' % appid, headers=self._headers).text, 'html.parser')
        app_info = {
            'app_id': appid
        }
        info_tb = app_page.find('div', 'app-row')
        app_info['app_type'] = info_tb.find('td', {'itemprop': 'applicationCategory'}).string
        app_info['app_name'] = info_tb.find('td', {'itemprop': 'name'}).string
        app_info['app_developer'] = info_tb.find('tbody').find_all('tr')[3].find_all('td')[1].find_next().get_text()
        app_info['app_publisher'] = info_tb.find('tbody').find_all('tr')[4].find_all('td')[1].find_next().get_text()
        app_info['rating'] = info_tb.find('meta', {'itemprop': 'ratingValue'})['content'] + '%'
        # print app_info
        return app_info


if __name__ == '__main__':
    si = SteamItem()
    si.get_app_info('570')