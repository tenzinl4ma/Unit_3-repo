
### Python Code
```.py
from kivy.lang import Builder
from kivymd.app import MDApp

class MyApp(MDApp):
    def build(self):
        return Builder.load_file("quiz037.kv")  
MyApp().run()
```