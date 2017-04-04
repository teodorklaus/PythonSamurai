__author__ = 'Ihor'
# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, send_from_directory
from Fesianov_Ihor.city_page.weather.weather_service import WeatherService
from Fesianov_Ihor.city_page.pictures.pictures_service import PicturesService
app = Flask(__name__)

WEATHER_SERVICE = WeatherService()


def get_weather_and_coord(city_name):
    if city_name:
        weather = WEATHER_SERVICE.get_weather(city_name)
        return weather.get_main_info_separated(), weather.coord()
    return '', ''


@app.route('/', methods=['GET', 'POST'])
def index():
    city_name = request.form.get('city')
    weather_info, coord = get_weather_and_coord(city_name)
    num_of_pictures = 16
    pictures_urls = PicturesService(city_name).get_pictures_url(num_of_pictures)
    return render_template('index.html',
                           weather_info=weather_info,
                           pictures_urls=pictures_urls,
                           coord=coord)


# todo how to use static files in flask
@app.route(r'/css/<path:path>')
def send_css(path):
    return send_from_directory('/templates', path)

if __name__ == '__main__':
    app.run(debug=True)