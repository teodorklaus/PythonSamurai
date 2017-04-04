__author__ = 'Ihor'

from datetime import datetime


class WeatherController:
    @staticmethod
    def save_to_json(weather):
        filename = '{}_{}_{}.json'.format(weather.city_name(), 'weather',
                                          datetime.now().strftime('%c').replace(':', '.').replace(' ', '_'))
        path = '..//json_files//{}.json'.format(filename)
        with open(path, 'w') as outfile:
            outfile.write(weather.to_json())
        return path[1:]
