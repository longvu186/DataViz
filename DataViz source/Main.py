from kivy.lang import Builder
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.image import Image
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from VizModules.BarChartRace import BarChartRaceScreen


class MyScreenManager(ScreenManager):
    pass


class ImageButton(ButtonBehavior, Image):
    pass


class MainMenu(Screen):
    pass


class MainApp(App):
    def build(self):
        return MyScreenManager()


if __name__ == "__main__":
    MainApp().run()