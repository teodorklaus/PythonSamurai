__author__ = 'Ihor'

import unittest
import os.path
from Fesianov_Ihor.city_information.weather_controller import WeatherController
from Fesianov_Ihor.city_information.weather_service import WeatherService


class TestWeatherController(unittest.TestCase):
    def test_save_to_json(self):
        test_weather_servise = WeatherService()
        test_weather = test_weather_servise.get_weather('Kyiv')
        filename = WeatherController.save_to_json(test_weather)
        self.assertTrue(os.path.isfile(filename))
