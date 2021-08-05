from kivy.app import App
from kivy.uix.button import Button
class ButtonApp(App):
    def build(self):
        Press = Button(text ="Press me",
                   font_size ="20sp",
                   background_color =(1, 1, 1, 1),
                   color =(1, 1, 1, 1),
                   size =(32, 32),
                   size_hint =(.2, .2),
                   pos =(300, 250))
        Press.bind(on_press = self.callback)
        return Press    
    def callback(self, event):
        print("Button pressed")
root = ButtonApp()
root.run()
