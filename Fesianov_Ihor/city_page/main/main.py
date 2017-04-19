__author__ = 'Ihor'
# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, jsonify
from Fesianov_Ihor.city_page.weather.weather_service import WeatherService
from Fesianov_Ihor.city_page.pictures.pictures_service import PicturesService
app = Flask(__name__)

WEATHER_SERVICE = WeatherService()
NUM_OF_PICTURES = 16


def get_weather_and_coord(city_name):
    weather = WEATHER_SERVICE.get_weather(city_name)
    return weather.get_main_info_dict(), weather.coord()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/process', methods=['POST'])
def process():
    city_name = request.form.get('city_name')
    if city_name:
        weather_info, coord = get_weather_and_coord(city_name)
        pictures_urls = PicturesService(city_name).get_pictures_url(NUM_OF_PICTURES)
        return jsonify(
            {
                'weather_info': weather_info,
                'pictures_urls': pictures_urls,
                'coord': coord
            }
        )
    return jsonify({'error': 'Missing data!'})


if __name__ == '__main__':
    app.run(debug=True)