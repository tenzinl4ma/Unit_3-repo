from kivy.app import App
from kivy.uix.widget import Widget

from kivy.lang import Builder
from kivy.core.window import Window

Window.size = (500, 700)
Builder.load_file('main.kv')
class MyLayout(Widget):
    def clear(self):
        self.ids.cal_input.text = "0"

    def buttonpress(self, button):
        prev = self.ids.cal_input.text

        if prev == "0" and button != "=":
            self.ids.cal_input.text = f"{button}"

        elif button == "=":
            if prev == "3561":
                self.ids.cal_input.text = "my secret"
            else:
                try:
                    result = str(eval(prev))  # Evaluate the expression
                    self.ids.cal_input.text = result
                except Exception as e:
                    self.ids.cal_input.text = "Error"
        else:
            self.ids.cal_input.text = f"{prev}{button}"

class CalculatorApp(App):
    def build(self):
        return MyLayout()

if __name__ == "__main__":
    CalculatorApp().run()
