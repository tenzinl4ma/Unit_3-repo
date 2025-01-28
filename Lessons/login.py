from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
import mylib

class LoginScreen(MDScreen):
    def acc_register(self):
        self.parent.current = "register" 
    def accountcreated(self):
        print("Account was succesfully Created")
        
class RegisterScreen(MDScreen):
    def try_register(self):
        print('user try to register')



class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "BlueGray"
        return Builder.load_file('login.kv')
    def limit_password_input(self, text_field):
        if len(text_field.text) > 16:
            text_field.text = text_field.text[:16]
        elif len(text_field.text) >7:
            print('Password not strong at all')
    def build(self):
        query_table = """CREATE TABLE IF NOT EXISTS user(
            id INTEGER PRIMARY KEY,
            username TEXT UNIQUE,
            password VARCHAR(256)
            email TEXT UNIQUE)
            """
        x = DatabaseManager(name= "login.sql")
        x.run_save(query= query_table)
        x.close()
        
MainApp().run()


