from kivymd.app import MDApp


class example2(MDApp):
    def build(self):
        return
    def change_label(self):
        print("hello, the button was pressed")
        self.root.ids.my_label.txt = "Bob smith"
    
test =example2()
test.run()
