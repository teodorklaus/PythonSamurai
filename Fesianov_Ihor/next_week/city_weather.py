__author__ = 'Ihor'

import urllib.request
import json
import io
from datetime import datetime


class WeatherService:
    def __init__(self, key):
        self.key = key
    # todo use types for better documenting
    def get_weather(self, city_name):
        """
        1. Make request to server
        2. Get json object
        3. Convert json obj to python obj
        4. Return py obj
        :param city_name:
        :return: py obj
        """
        # todo exract url as constant or class field and do the same to key
        response = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q={}&APPID={}'
                                          .format(city_name, self.key))
        weather_json = response.read()
        return Weather(json.loads(weather_json))


class Weather:
    def __init__(self, weather_dict):
        self.weather_dict = weather_dict

    def city_name(self):
        return self.weather_dict['name']

    def description(self):
        return self.weather_dict['weather'][0]['description']

    def temp(self):
        return self.weather_dict['main']['temp']

    def pressure(self):
        return self.weather_dict['main']['pressure']

    def humidity(self):
        return self.weather_dict['main']['humidity']

    def to_json(self):
        return json.dumps(
            {
                'Name': self.city_name(),
                'Description': self.description(),
                'Temperature': self.temp(),
                'Pressure': self.pressure(),
                'Humidity': self.humidity()
            }
        )


class Application:
    def __init__(self):
        # todo get accessKey from propertyFile -> see how to work with properties
        self.key = '4a98e3f0ed18bd280f800d713825cc19'
        self.service = WeatherService(self.key)

    def run(self):
        while True:
            user_choice = self.main_menu()
            if self.is_exit(user_choice):
                break

    def main_menu(self):
        # you may group next three lines as show menu method
        print('1.Show weather')
        print('2.Show detailed weather')
        print('3.Exit')
        user_choice = self.get_user_choice()
        if user_choice == 1:
            self.show_weather()
        elif user_choice == 2:
            self.show_detailed_weather()
        elif user_choice != 3:
            self.show_try_again()
        return user_choice

    def show_detailed_weather(self):
        city_name = input('Enter city name:\n')
        weather = self.service.get_weather(city_name)
        # perhaps weather would have self method that returns str presentation
        print('Description: {}'.format(weather.description()))
        print('Temperature: {}{}'.format(round(weather.temp() - 273), ' degree C'))
        print('Pressure: {}{}'.format(weather.pressure(), ' hPa'))
        print('Humidity: {}{}\n'.format(weather.humidity(), '%'))
        self.show_save_menu(weather)

    def show_weather(self):
        city_name = input('Enter city name:\n')
        weather = self.service.get_weather(city_name)
        print('Description: {}'.format(weather.description()))
        print('Temperature: {}{}\n'.format(round(weather.temp() - 273), ' degree C'))
        self.show_save_menu(weather)

    def get_user_choice(self):
        user_choice = input()
        if self.represents_int(user_choice):
            return int(user_choice)
        return None

    def show_save_menu(self, weather):
        user_choice = input('Save file?[y/n]: ')
        if user_choice == 'y':
            self.save_to_json(weather)

    @staticmethod
    def save_to_json(weather):
        filename = '{}_{}_{}.json'.format(weather.city_name(), 'weather',
                                          datetime.now().strftime('%c').replace(':', '.').replace(' ', '_'))
        with io.open(filename, 'w') as outfile:
            outfile.write(weather.to_json())
            outfile.close()
        print(''''File '{}' has been saved by me'''.format(filename))

    @staticmethod
    def show_try_again():
        print('Your choice is not correct. Try again!')

    @staticmethod
    def is_exit(user_choice):
        return user_choice == 3

    @staticmethod
    def represents_int(string):
        try:
            int(string)
            return True
        except ValueError:
            return False


Application().run()
