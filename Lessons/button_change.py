from kivymd.app import MDApp
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.button import MDFlatButton

class CapitalCityApp(MDApp):
    def build(self):
     
        return BoxLayout(orientation='vertical')

    def label_change(self, country):

        capitals = {
            'Nepal': 'Kathmandu',
            'Japan': 'Tokyo',
            'USA': 'Washington, D.C.',
            'India': 'New Delhi',
            'China': 'Beijing'
        }
        
 
        self.root.ids.my_label.text = f"Capital of {country}: {capitals.get(country, 'Unknown')}"

if __name__ == "__main__":
    CapitalCityApp().run()
