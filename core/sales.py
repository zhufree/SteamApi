#coding: utf-8
from requests import get
from bs4 import BeautifulSoup as BS
import re

class SteamSales(object):
    """docstring for SteamSales"""
    def __init__(self):
        super(SteamSales, self).__init__()
        # self.arg = arg
        headers = {
            'Host': 'steamdb.info',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
            'Accept-Encoding': 'gzip, deflate',
            'Referer': 'http://www.baidu.com',
            'Connection': 'keep-alive',
            'Cache-Control': 'max-age=0',
        }
        self.all_sales_page = BS(get('https://steamdb.info/sales/?merged=true&cc=cn', headers=headers).text, 'html.parser')

    def get_all_sales(self, count):
        all_sales_list = []
        sales = self.all_sales_page.find_all('tr', 'appimg')
        # print sales[:10]
        for s in sales[:count]:
            info_tds = s.find_all('td')

            s_info = {}
            s_info['discount'] = info_tds[3].string
            s_info['price'] = info_tds[4].string
            end_in = info_tds[5]  # 不一定有截止日期
            if end_in['data-sort'] == '0':
                s_info['end_in'] = '-'
            else:
                s_info['end_in'] = info_tds[5]['title']
            s_info['start_at'] = info_tds[7]['title']

            s_info['rating'] = info_tds[6]['data-sort'] + '%'

            item_info = s.find('i', 'subinfo').get_text()
            if ', ' in item_info:
                item_info = item_info.split(', ')
                s_info['item_type'] = item_info[0]
                s_info['discount_info'] = item_info[1]

            else:
                s_info['item_type'] = item_info
            

            if s_info['item_type'] in ['Game', 'DLC', 'Application']:
                s_info['item_name'] = info_tds[2].find('a').string
                s_info['item_id'] = s['data-appid']
                s_info['sale_img'] = 'https://steamdb.info/static/camo/apps/' + s_info['item_id'] + '/capsule_sm_120.jpg'
            else:
                s_info['item_name'] = info_tds[2].find('a').string
                s_info['item_id'] = s['data-subid']
                s_info['sale_img'] = 'https://steamdb.info/static/camo/subs/' + s_info['item_id'] + '/capsule_sm_120.jpg'
            all_sales_list.append(s_info)
        return all_sales_list
    
    def get_sales_by_rating(self, count):
        sort = sorted(self.get_all_sales(count), key=lambda item:int(item['rating'][:-1]), reverse=True)
        return sort

    def get_sales_by_price(self, count):
        sort = sorted(self.get_all_sales(count), key=lambda item:int(item['price'][1:-3]))
        return sort

if __name__ == '__main__':
    ss = SteamSales()
    ss.get_all_sales(None)