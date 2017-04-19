__author__ = 'Ihor'

import urllib.request
import os.path
import unittest

from Fesianov_Ihor.city_information.weather_service import WeatherService


class TestWeatherService(unittest.TestCase):
    FILENAME = WeatherService.FILENAME

    def test_read_properties(self):
        self.assertTrue(os.path.isfile(self.FILENAME))

    def test_get_weather(self):
        with self.assertRaises(urllib.error.URLError):
            # todo get from config
            urllib.request.urlopen('http://api.openweatherma.org/data/2.5/weather?')
            urllib.request.urlopen('http://api.openweatherma.org/data/2.5/weather?' + 'q={}&APPID={}'
                                   .format('Kyiv', '153'))

if __name__ == '__main__':
    unittest.main()


