from kivymd.app import MDApp
from kivy.lang import Builder

class Prac(MDApp):
    def build(self):
        Builder.load_file("prac.kv")
        return Builder.load_string("")

Prac().run()
