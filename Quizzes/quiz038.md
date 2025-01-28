# Python Code
```.py
from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang import Builder

# Define the screens
class MysteryPageA(Screen):
    pass

class MysteryPageB(Screen):
    pass

# Main app class
class MDApp(MDApp):
    def build(self):
        # Load the Kivy file
        return Builder.load_file("quiz038.kv")

# Run the app
if __name__ == '__main__':
    MDApp().run()
````