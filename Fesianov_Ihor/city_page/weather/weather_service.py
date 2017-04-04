__author__ = 'Ihor'

from Fesianov_Ihor.useful.web import read_properties
import urllib.request
import json

from .weather import Weather


class WeatherService:

    FILENAME = 'D:\Python_lessons\study\PythonSamurai\Fesianov_Ihor\city_page\weather\data_files\conf.properties'
    conf = read_properties(FILENAME)
    URL, KEY = conf['URL'], conf['KEY']

    @staticmethod
    def read_properties(filename):
        data = {}
        with open(filename) as file:
            for line in file:
                name, value = line.split('=', 1)
                data[name.strip()] = value.strip()
        return data['URL'], data['KEY']

    @staticmethod
    def get_weather(city_name: str) -> Weather:
        """
        1. Make request to server
        2. Get json object
        3. Convert json obj to python obj
        4. Return py obj
        :param city_name:
        :return: py obj
        """
        response = urllib.request.urlopen('{0}q={1}&APPID={2}'
                                          .format(WeatherService.URL, city_name, WeatherService.KEY))
        weather_json = response.read()
        return Weather(json.loads(weather_json))

