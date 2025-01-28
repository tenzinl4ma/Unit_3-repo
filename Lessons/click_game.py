from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRaisedButton

class ClickGame(MDApp):
    def build(self):
        screen = Screen()


        self.count_label = MDLabel(
            text="Your Name",
            halign="center",
            font_size="100pt",
            color=(0, 1, 0, 1),  
            size_hint=(.4, 0.3),
            pos_hint={"center_x": 0.25, "center_y": 0.7}
        )
        screen.add_widget(self.count_label)


        self.button = MDRaisedButton(
            text="Change the Name",
            size_hint=(0.5, 0.1),
            font_size="34pt",
            md_bg_color=(1, 0, 0, 1), 
            pos_hint={"center_x": 0.75, "center_y": 0.3},
            on_press=self.countt
        )
        screen.add_widget(self.button)

        return screen

    def countt(self, instance):

        self.countt_value = int(self.count_label.text) + 1
        self.count_label.text = str(self.countt_value)

ClickGame().run()