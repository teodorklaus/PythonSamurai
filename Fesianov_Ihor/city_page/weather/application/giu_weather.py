from tkinter import *
import tkinter.messagebox

from ..weather_service import WeatherService
from ..weather_controller import WeatherController


class EnterCityName:
    def __init__(self, master, weather):
        frame = Frame(master, width=200, height=100, bg="darkred")
        frame.pack(side='top')

        self.city_name = ''
        self.weather = weather

        self.label = Label(frame, text='Enter city name', fg='white', bg='darkred')
        self.label.pack()

        self.entry = Entry(frame, width=20, bd=2)
        self.entry.pack()

        self.button = Button(frame, text='Search')
        self.button.bind("<Button-1>", self.do_all)
        self.button.pack(side=RIGHT)

    def do_all(self, event):
        self.save_city_name()
        self.weather.show_weather(self.city_name)

    def save_city_name(self):
        self.city_name = self.entry.get()

    def get_city_name(self):
        return self.city_name


class WeatherFrame:
    def __init__(self, master):
        frame = Frame(master, width=200, height=100, bg="darkblue")
        frame.pack(fill='both')
        self.label = Label(frame, text='', fg='white', bg='darkblue')

    @staticmethod
    def get_str_weather(city_name):
        weather = WeatherFrame.get_weather(city_name)
        return weather.str_presentation()

    @staticmethod
    def get_weather(city_name):
        weather_service = WeatherService()
        return weather_service.get_weather(city_name)

    def show_weather(self, city_name):
        self.label.configure(text=self.get_str_weather(city_name))
        self.label.pack()


class ImportExportButtons:
    def __init__(self, master, weather):
        frame = Frame(master, width=200, height=100, bg="darkblue")
        frame.pack(fill='both')

        self.weather = weather

        self.import_button = Button(frame, text='Import', width=75)
        self.import_button.pack()

        self.export_button = Button(frame, text='Export', width=75)
        self.export_button.pack()
        self.export_button.bind("<Button-1>", self.show_save_decision)

    def show_save_decision(self, event):
        answer = tkinter.messagebox.askquestion('Save file?', 'Do you want to save data?')
        if answer == 'yes':
            self.save_to_json()

    def save_to_json(self):
        filename = WeatherController.save_to_json(self.weather)
        tkinter.messagebox.showinfo('save', 'Data has saved to '.format(filename))


def do_nothing():
    print("ok ok I won't")


def menu():
    main_menu = Menu(root)
    root.config(menu=main_menu)

    sub_menu = Menu(main_menu)
    main_menu.add_cascade(label='File', menu=sub_menu)
    sub_menu.add_command(label='New project', command=do_nothing)
    sub_menu.add_command(label='New', command=do_nothing)
    sub_menu.add_separator()
    sub_menu.add_command(label='Exit', command=do_nothing())


root = Tk()
root.geometry('450x450')
root.title('City information')


weather = WeatherFrame(root)
enter = EnterCityName(root, weather)
ie_buttons = ImportExportButtons(root, weather.get_weather(enter.city_name))


root.mainloop()
