__author__ = 'Ihor'

import json


class Weather:
    def __init__(self, weather_dict):
        self.weather_dict = weather_dict

    def city_name(self) -> str:
        return self.weather_dict['name']

    def description(self) -> str:
        return self.weather_dict['weather'][0]['description']

    def temp(self) -> int:
        return self.weather_dict['main']['temp']

    def pressure(self) -> str:
        return self.weather_dict['main']['pressure']

    def humidity(self) -> str:
        return self.weather_dict['main']['humidity']

    def coord(self):
        return self.weather_dict['coord']

    def to_json(self) -> json:
        return json.dumps(self.get_main_info_dict())

    def str_presentation(self):
        des_str = 'Description: {}\n'.format(self.description())
        temp_str = 'Temperature: {}{}\n'.format(round(self.temp() - 273), ' degree C')
        press_str = 'Pressure: {}{}\n'.format(self.pressure(), ' hPa')
        hum_str = 'Humidity: {}{}\n'.format(self.humidity(), '%')
        return des_str + temp_str + press_str + hum_str

    def get_main_info_dict(self) -> dict:
        return dict(self.get_main_info_list())

    def get_main_info_list(self) -> dict:
        return [
            ('Name', self.city_name()),
            ('Description', self.description().capitalize()),
            ('Temperature', '{} degree C'.format(round(self.temp() - 273))),
            ('Pressure', '{} hPa'.format(self.pressure())),
            ('Humidity', '{} %'.format(self.humidity()))
        ]

    def get_main_info_separated(self):
        info = {'signs': [], 'values': []}
        for el in self.get_main_info_list():
            info['signs'].append(el[0])
            info['values'].append(el[1])
        return info

