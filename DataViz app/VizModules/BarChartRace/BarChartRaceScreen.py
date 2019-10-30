import kivy
import os
from kivy.lang import Builder
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import Screen
from VizModules.BarChartRace import BarChartRace

Builder.load_file('VizModules/BarChartRace/BarChartRaceScreen.kv')

with open('VizModules/BarChartRace/Help.txt') as f:
    text = f.read()


class HelpPopup(Popup):
    text = text


class BarChartRaceScreen(Screen):
    Chart = BarChartRace.BarChartRaceClass()

    def get_settings(self):
        setattr(self.Chart, 'title', self.ids.title.text)
        setattr(self.Chart, 'time_text_color', self.ids.time_text_color.text)
        setattr(self.Chart, 'value_format', self.ids.value_format.text)
        setattr(self.Chart, 'transparent_background', self.ids.transparent_background.active)
        setattr(self.Chart, 'floating_point', int(self.ids.floating_point.text))
        setattr(self.Chart, 'data_interpolation', int(self.ids.data_interpolation.text))
        setattr(self.Chart, 'fps', int(self.ids.fps.text))
        setattr(self.Chart, 'font_size', int(self.ids.font_size.text))

    @staticmethod
    def edit_excel():
        dirpath = os.getcwd()
        os.startfile(os.path.join(dirpath, 'VizModules/BarChartRace/BarChartRace.xlsx'))

    def preview(self):
        self.get_settings()
        self.Chart.preview()

    def export(self):
        self.get_settings()
        self.Chart.export()





