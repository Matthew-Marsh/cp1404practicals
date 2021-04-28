"""
Practical 7 - Convert miles to km

Matthew Marsh
"""
from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

__author__ = "Matthew Marsh"

MILE_TO_KM = 1.61


class ConvertMilesToKmApp(App):
    def build(self):
        """ build the app from the kv file """
        Window.size = (600, 300)
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def calculate_km_from_miles(self, miles=0):
        """ calculate the km converted from the input miles """
        result = miles * MILE_TO_KM
        self.root.ids.output_number.text = str(result)


ConvertMilesToKmApp().run()
