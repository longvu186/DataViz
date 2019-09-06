import kivy
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from VizModules.BarChartRace import BarChartRace

Builder.load_string('''
<BarChartRaceScreen>:
#:import SlideTransition kivy.uix.screenmanager.SlideTransition
    name: 'BarChartRace'
    BoxLayout:
        orientation: 'vertical'

        BoxLayout:
            # Top bar
            orientation: 'horizontal'
            size_hint_y: None
            height: 50
            Label:
                canvas:
                    Color:
                        rgba: .47,.43,.848,0.5
                    Rectangle:
                        pos: self.pos
                        size: self.size
                text_size: self.size
                halign: 'left'
                valign: 'middle'
                padding_x: 20
                font_size: 20
                text: 'Bar Chart Race'

        BoxLayout:
            orientation: 'horizontal'

            BoxLayout:
                # Layout of the control panel on the left
                size_hint_x: None
                width: 200
                canvas:
                    Color:
                        rgba: .47,.43,.848,0.5
                    Rectangle:
                        pos: self.pos
                        size: self.size
                orientation: 'vertical'

                AnchorLayout:
                    anchor_x: 'center'
                    Image:
                        source: 'VizModules/BarChartRace/BarChartRace.jpg'

                AnchorLayout:
                    anchor_x: 'center'
                    Button:
                        size_hint_y: None
                        size_hint_x: None
                        height: 50
                        width: 100
                        text: 'Help'

                AnchorLayout:
                    anchor_x: 'center'
                    anchor_y: 'top'
                    Button:
                        size_hint_y: None
                        size_hint_x: None
                        height: 50
                        width: 100
                        text: 'Back'
                        on_release:
                            app.root.current = 'MainMenu'
                            app.root.transition = SlideTransition(direction = 'left')

            GridLayout:
                cols: 1
                rows: 2
                # Layout of the input fields
                orientation: 'vertical'

                # Input fields
                # -------------------------------------------------------
                StackLayout:
                    padding: 30
                    spacing: 20

                    BoxLayout:
                        orientation: 'horizontal'
                        size_hint_y: None
                        size_hint_x: None
                        height: 50
                        width: 400
                        Label:
                            size_hint_x: None
                            width: 200
                            text: 'Title'
                        AnchorLayout:
                            anchor_y: 'center'
                            TextInput:
                                id: title
                                size_hint_y: None
                                height: 30

                    BoxLayout:
                        orientation: 'horizontal'
                        size_hint_y: None
                        size_hint_x: None
                        height: 50
                        width: 400
                        Label:
                            size_hint_x: None
                            width: 200
                            text: 'Color of time indicator'
                        AnchorLayout:
                            anchor_y: 'center'
                            TextInput:
                                id: time_text_color
                                size_hint_y: None
                                height: 30
                                text: 'black'

                    BoxLayout:
                        orientation: 'horizontal'
                        size_hint_y: None
                        size_hint_x: None
                        height: 50
                        width: 400
                        Label:
                            size_hint_x: None
                            width: 200
                            text: 'Value format'
                        AnchorLayout:
                            anchor_y: 'center'
                            TextInput:
                                id: value_format
                                size_hint_y: None
                                height: 30
                                text: '{}'

                    BoxLayout:
                        orientation: 'horizontal'
                        size_hint_y: None
                        size_hint_x: None
                        height: 50
                        width: 400
                        Label:
                            size_hint_x: None
                            width: 200
                            text: 'Transparent background'
                        AnchorLayout:
                            anchor_y: 'center'
                            CheckBox:
                                id: transparent_background

                    BoxLayout:
                        orientation: 'horizontal'
                        size_hint_y: None
                        size_hint_x: None
                        height: 50
                        width: 400
                        Label:
                            size_hint_x: None
                            width: 200
                            text: 'Floating point'
                        AnchorLayout:
                            anchor_y: 'center'
                            TextInput:
                                id: floating_point
                                size_hint_y: None
                                height: 30
                                text: '0'

                    BoxLayout:
                        orientation: 'horizontal'
                        size_hint_y: None
                        size_hint_x: None
                        height: 50
                        width: 400
                        Label:
                            size_hint_x: None
                            width: 200
                            text: 'Data interpolation'
                        AnchorLayout:
                            anchor_y: 'center'
                            TextInput:
                                id: data_interpolation
                                size_hint_y: None
                                height: 30
                                text: '20'

                    BoxLayout:
                        orientation: 'horizontal'
                        size_hint_y: None
                        size_hint_x: None
                        height: 50
                        width: 400
                        Label:
                            size_hint_x: None
                            width: 200
                            text: 'FPS'
                        AnchorLayout:
                            anchor_y: 'center'
                            TextInput:
                                id: fps
                                size_hint_y: None
                                height: 30
                                text: '30'

                    BoxLayout:
                        orientation: 'horizontal'
                        size_hint_y: None
                        size_hint_x: None
                        height: 50
                        width: 400
                        Label:
                            size_hint_x: None
                            width: 200
                            text: 'Font size'
                        AnchorLayout:
                            anchor_y: 'center'
                            TextInput:
                                id: font_size
                                size_hint_y: None
                                height: 30
                                text: '25'


                # -------------------------------------------------------

                BoxLayout:
                    size_hint_y: 0.25
                    BoxLayout:
                        orientation: 'horizontal'
                        AnchorLayout:
                            Button:
                                anchor_x: 'center'
                                size_hint_x: 0.5
                                size_hint_y: 0.5
                                text: 'Preview'
                                on_release: root.preview()


                        AnchorLayout:
                            Button:
                                anchor_x: 'center'
                                size_hint_x: 0.5
                                size_hint_y: 0.5
                                text: 'Export'
                                on_release: root.export()
''')


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

    def preview(self):
        self.get_settings()
        self.Chart.preview()

    def export(self):
        self.get_settings()
        self.Chart.export()





