from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen


class MysteryPageA(MDScreen):
    def mysterya(self):
        self.parent.current = "register" 
    def mysteryb(self):
        pass
        
        
        
class MysteryPageB(MDScreen):
    pass
class quiz37(MDApp):
    pass
t = quiz37()
t.run()