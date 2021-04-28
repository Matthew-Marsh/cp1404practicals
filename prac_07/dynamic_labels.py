"""
Practical 7 - Dyanmic Labels

Matthew Marsh
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label

__author__ = "Matthew Marsh"


class DynamicLabelsApp(App):
    """Add Dynamic labels from a list of names to Kivy UI."""

    def __init__(self, **kwargs):
        """ Initialise the main app. """
        super().__init__(**kwargs)
        self.names = ['Alice', 'Bob', 'Thomas', 'Belinda', 'Charlie']

    def build(self):
        """Build the interface for the dynamic labels."""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_labels()
        return self.root

    def create_labels(self):
        """Creates labels from list of names and adds them to the Kivy UI."""
        for name in self.names:
            new_label = Label(text=name)
            self.root.ids.names_box.add_widget(new_label)


DynamicLabelsApp().run()
