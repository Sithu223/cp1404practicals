

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.properties import StringProperty


NEW_COLOUR = (1, 0, 0, 1)  # RGBA for red
ALTERNATIVE_COLOUR = (1, 0, 1, 1)  # RGBA for magenta


class DynamicWidgetsApp(App):
    """Main program - Kivy app to demo dynamic widget creation."""
    status_text = StringProperty()

    def __init__(self, **kwargs):
        """Construct main app."""
        super().__init__(**kwargs)
        # basic data (model) example - dictionary of names: phone numbers
        self.name_to_phone = {"Bob Brown": "0414144411", "Cat Cyan": "0441411211", "Oren Ochre": "0432123456"}

    def build(self):
        """Build the Kivy GUI."""
        self.title = "Dynamic Widgets"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_widgets()
        return self.root

    def create_widgets(self):
        """Create buttons from data and add them to the GUI."""
        for name in self.name_to_phone:
            # create a button for each data entry, specifying the text
            temp_button = Button(text=name)
            temp_button.bind(on_press=self.press_entry)
            # set the button's background colour
            temp_button.background_color = NEW_COLOUR
            # add the button to the "entries_box" layout widget
            self.root.ids.entries_box.add_widget(temp_button)