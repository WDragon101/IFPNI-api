import requests
from bs4 import BeautifulSoup
import time


class IFPNI():
    def __init__(self, source='', name='', author='', rankID=[], originalSpelling='', yearFrom='',
                 yearTo='', paleoID=[]):
        self.source = source
        self.name = name
        self.author = author
        self.rankID = rankID
        self.originalSpelling = originalSpelling
        self.yearFrom = yearFrom
        self.yearTo = yearTo
        self.paleoID = paleoID
        self.formIndex = 'def'
        self.isExtended = 1
        self.submitForm = 'Search'

        self.ifpni_org = 'http://www.ifpni.org'

        self.ifpni_order_org = {'suprageneric': '/supragenus.htm',
                                'generic': '/genus.htm',
                                'infrageneric': '/infragenus.htm',
                                'species': '/species.htm',
                                'infraspecies': '/infraspecies'}
        self.ifpni_common_url_part = '&'.join([f"formIndex={self.formIndex}", f"name={self.name}",
                                               f"isExtended={self.isExtended}", f"author={self.author}",
                                               f"originalSpelling={self.originalSpelling}", f"yearFrom={self.yearFrom}",
                                               f"yearTo={self.yearTo}", f"submitForm={self.submitForm}"])
        self.ifpni_special_url_part = {'suprageneric': '&'.join([f"rankID%5B%5D={str(ri)}" for ri in self.rankID]),
                                       'generic': '&'.join([f"rankID%5B%5D={str(ri)}" for ri in self.rankID]),
                                       'infrageneric': '&'.join([f"rankID%5B%5D={str(ri)}" for ri in self.rankID]),
                                       'species': '&'.join([f"rankID%5B%5D={str(ri)}" for ri in self.rankID]) +
                                                  '&'.join([f"paleoID={str(pi)}" for pi in self.paleoID]),
                                       'infraspecies': '&'.join([f"rankID%5B%5D={str(ri)}" for ri in self.rankID]) +
                                                       '&'.join([f"paleoID={str(pi)}" for pi in self.paleoID]), }

        self.headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, '
                                      'like Gecko) Chrome/103.0.5060.66 Safari/537.36 Edg/103.0.1264.44'}

        self.url = ''
        self.pages = 0
        self.hrefs = []
        self.items = []

    def url_build(self):
        self.url = self.ifpni_org + self.ifpni_order_org[self.source] + '?' + '&'.join([self.ifpni_common_url_part, self.ifpni_special_url_part[self.source]])

    def judge_items(self):
        self.hrefs.clear()
        time.sleep(0.3)
        res = requests.get(url=self.url, headers=self.headers)
        soup = BeautifulSoup(res.text, 'html.parser')
        num = int(soup.find('h4').text.split(' ')[-1])
        if num != 0:
            self.pages = round(num/10)
        for i in range(self.pages):
            time.sleep(0.3)
            url = self.url + f"&page={i+1}"
            pres = requests.get(url=url, headers=self.headers)
            psoup = BeautifulSoup(pres.text, 'html.parser')
            items = psoup.find_all('span', class_='list-group-item')
            for item in items:
                href = item.find('h1', class_='lead list-group-item-heading').find('a')['href']
                self.hrefs.append(f"http://www.ifpni.org{href}")

    def claw_item(self):
        count = 0
        for href in self.hrefs:
            count += 1
            res = requests.get(url=href, headers=self.headers)
            soup = BeautifulSoup(res.text, 'html.parser')
            id_pre = soup.find('div', class_='panel panel-default').find('div', class_='panel-heading').find_all('span')
            id = id_pre[1].text.split(':')[-1]
            rank = id_pre[2].text
            title = soup.find('div', class_='panel-body').find('h1').text
            nomen = soup.find('div', id='nomenQuote').text
            table = soup.find('dl', class_='dl-horizontal')
            keys = []
            for dt in table.find_all('dt'):
                dt = dt.text.strip().replace('\n', '')
                keys.append(f'''{dt}''')
            values = []
            for dd in table.find_all('dd'):
                dd = dd.text.strip().replace('\n', '')
                values.append(f'''{dd.text}''')
            item = {'id': id, 'rank': rank, 'title': title, 'nomen': nomen, 'tabel': dict(zip(keys, values))}
            self.items.append(item)
        print('search over')

    def inner_pro(self):
        self.url_build()
        self.judge_items()
        self.claw_item()
