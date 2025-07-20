

from kivy.app import App
from kivy.lang import Builder

__author__ = 'Sithu Hein'

MILES_TO_KM = 1.60934


class MilesConverterApp(App):
    """ MilesConverterApp is a Kivy App for converting miles to kilometres """

    def build(self):
        """ build the Kivy app from the kv file """
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')

    def handle_calculate(self):
        """ handle calculation (could be button press or other call), output result to label widget """
        value = self.get_validated_miles()
        result = value * MILES_TO_KM
        self.root.ids.output_label.text = str(result)