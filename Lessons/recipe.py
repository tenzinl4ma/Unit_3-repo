from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen

class IntroScreen(MDScreen):
    def next(self):
        self.parent.current = "PrepareScreen"
    

class PrepareScreen(MDScreen):
    def back(self):
        self.parent.current = "IntroScreen"
    def add_flour(self):
        if self.ids.flour.active:
            print('Flour was added')
        else:
            print('Flour was removed')

class BakeScreen(MDScreen):
    pass
class recipe(MDApp):
    def build(self):
        return 
t = recipe()
t.run()
    
    