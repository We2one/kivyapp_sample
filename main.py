from kivy.app import App
from kivy.uix.button import Button


class ButtonApp(App):
    def build(self):
        return Button(text="Button")


ButtonApp().run()
