from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
import ok
from kivy.clock import Clock

class MyApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical')
        self.result_label = Label(text="")
        self.layout.add_widget(self.result_label)
        self.button = Button(text="Get Time")
        self.button.bind(on_press=self.get_time)
        self.layout.add_widget(self.button)
        self.loading_label = Label(text="Loading...")
        self.loading_label.opacity = 0
        self.layout.add_widget(self.loading_label)
        return self.layout

    def get_time(self, instance):
        self.loading_label.opacity = 1
        Clock.schedule_once(self.get_time_async, 0)

    def get_time_async(self, dt):
        current_time = ok.get_time()
        self.result_label.text = "Current Time: " + current_time
        self.loading_label.opacity = 0

MyApp().run()

