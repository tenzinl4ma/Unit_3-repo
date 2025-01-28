from kivymd.app import MDApp

class converter(MDApp):
    def build(self):
        return
    def yen_entered(self):
        yen = self.root.ids.user_input.text
        if yen.isdecimal():
            yen_amount = int(yen)
            self.yen_ammount = yen_amount
            
        else:
            self.root.ids.user_input.helper_text = 'enter the valid input'
            self.root.ids.user_input.error = True
            
    def convert(self,currency):
        options = {'usd': 150, 'cad':120}
        if currency in options:
            result = self.yen_ammount /options[currency]
            self.root.ids.user_input.text = f"{result}"
    
            
            
test = converter()
test.run()

