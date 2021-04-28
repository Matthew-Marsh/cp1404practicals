"""
Practical 7 - Convert miles to km

Matthew Marsh
"""
from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.app import StringProperty

__author__ = "Matthew Marsh"

MILE_TO_KM = 1.61


class ConvertMilesToKmApp(App):
    """ ConvertMilesToKm is a kivy app that takes a number of kms and converts it to miles"""
    kilometres = StringProperty()

    def build(self):
        """ build the app from the kv file """
        Window.size = (600, 300)
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def calculate_button_press(self):
        """ calculate the km converted from the input miles """
        try:
            self.kilometres = str(int(self.root.ids.input_number.text) * MILE_TO_KM)
        except ValueError:
            self.kilometres = '0.0'

    def handle_increment(self, number=0, increment=1):
        """ increase the input number by the increment """
        try:
            if number == "":
                number = 0
            number = int(number)
            number += increment
            self.root.ids.input_number.text = str(number)
            self.kilometres = str(number * MILE_TO_KM)
        except ValueError:
            self.kilometres = '0.0'


ConvertMilesToKmApp().run()
