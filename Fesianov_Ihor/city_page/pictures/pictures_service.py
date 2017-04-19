__author__ = 'Ihor'
# -*- coding: utf-8 -*-

from Fesianov_Ihor.useful.web import read_properties
from lxml import html
import requests


class PicturesService:
    FILENAME = 'D:\Python_lessons\study\PythonSamurai\Fesianov_Ihor\city_page\pictures\data_files\conf.properties'
    BROWSER_HEADERS = {'User-Agent': read_properties(FILENAME)['User-Agent']}

    def __init__(self, cityname):
        self.cityname = cityname
        self.url = read_properties(PicturesService.FILENAME)['URL'].replace('CITYNAME', str(cityname))

    def get_html(self) -> str:
        r = requests.get(self.url, headers=self.BROWSER_HEADERS)
        return r.text.encode()

    def get_pictures_url(self, pictures_num=8) -> list:
        tree = html.fromstring(self.get_html())
        return tree.xpath('//img[@class="rg_ic rg_i"][@data-src]/@data-src')[:pictures_num]

