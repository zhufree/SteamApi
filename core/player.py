#coding: utf-8
from requests import get
from bs4 import BeautifulSoup as BS
import re
import json

class SteamPlayer(object):
    """docstring for SteamPlayer"""
    def __init__(self):
        super(SteamPlayer, self).__init__()
        # self.arg = arg

    def get_basic_info(self, player):
        player_info = {}

        sdb_page = BS(get('https://steamdb.info/calculator/?player=%s&cc=cn' % player).text, 'html.parser')
        player_id = [s.string for s in sdb_page.find_all('span', 'select-me')]
        player_info['id'] = {
            'VanityURL': player_id[0],
            'steamID': player_id[1],
            'steam2ID': player_id[2],
            'steam3ID': player_id[3]
        }
        player_info['name'] = sdb_page.find('h1', 'header-title').a.string
        info_li = sdb_page.find('div', 'header-player').find('ul', 'clearfix').find_all('li')
        player_info['status'] = info_li[0].string # Online/Offline
        player_info['exp'] = info_li[1].find('span').string + 'XP'
        player_info['created-date'] = info_li[2].find('span')['title']
        player_info['last-online'] = info_li[3].find('span')['title']
        row_stats = sdb_page.find('div', 'row-stats')
        player_info['account-value'] = row_stats.find('b', 'number-price').string
        player_info['lowest-account-value'] = row_stats.find('b', 'number-price-lowest').string
        span2 = sdb_page.find_all('div','span2')
        player_info['level'] = span2[0].find('b', 'number').get_text().strip()
        player_info['games-owned'] = span2[1].find('b').string
        player_info['play-hours'] = span2[2].find('b').string

        steam_page = BS(get('https://steamcommunity.com/id/%s/' % player_info['id']['VanityURL']).text, 'html.parser')
        player_info['real-name'] = steam_page.find('div', 'header_real_name').find('bdi').string
        player_info['country'] = steam_page.find('img','profile_flag').string.strip()
        player_info['summary'] = steam_page.find('div', 'profile_summary').string.strip()
        print player_info
        return player_info

    def get_games_info(self, player):
        game_page = get('https://steamcommunity.com/id/%s/games/?tab=all' % player).text
        result = re.compile(r'rgGames = (\[.+\]);').search(game_page)
        games_info = json.loads(result.group(1))
        return games_info



if __name__ == '__main__':
    sp = SteamPlayer()
    # sp.get_basic_info('zhufree')
    print sp.get_games_info('zhufree')
