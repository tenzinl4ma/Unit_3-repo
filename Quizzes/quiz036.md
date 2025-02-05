# Python code
```.py
from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang import Builder


class Whitemode(Screen):
    pass
class Darkmode(Screen):
    pass

class MyApp(MDApp):
    def build(self):
        return Builder.load_file("quiz036.kv")
    def change_to_dark_mode(self):
        self.theme_cls.theme_style = "Dark"  
        self.root.get_screen("darkmode").md_bg_color = (0, 0, 0, 1)
        self.root.current = "darkmode"

    def change_to_light_mode(self):
        self.theme_cls.theme_style = "Light"  
        self.root.get_screen("whitemode").md_bg_color = (1, 1, 1, 1)
        self.root.current = "whitemode"


MyApp().run()
```
### Proof of work
