__author__ = 'Ihor'

from Fesianov_Ihor.city_page.weather.weather_service import WeatherService
from Fesianov_Ihor.city_page.weather.weather_controller import WeatherController


class Application:
    def __init__(self):
        self.service = WeatherService()
        self.weather_controller = WeatherController()

    def run(self):
        while True:
            user_choice = self.main_menu()
            if self.is_exit(user_choice):
                break

    @staticmethod
    def show_menu():
        print('1.Show weather')
        print('2.Show detailed weather')
        print('3.Exit')

    def main_menu(self):
        Application.show_menu()
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
        print(weather.str_presentation())
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

    def save_to_json(self, weather):
        filename = self.weather_controller.save_to_json(weather)
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

if __name__ == '__main__':
    Application().run()

