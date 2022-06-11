from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window

Window.size = (450, 650)

app_Builder = """
Screen:
    MDBoxLayout:
        orientation: 'vertical'
    MDLabel:
        text: 'Password Validator'
        halign: 'center'
        pos_hint: {'center_x': 0.5, 'center_y': 0.9}
        font_size: '50'
    MDTextField:
        hint_text: "Enter password to validate"
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        size_hint:0.5, None
    MDRaisedButton:
        text: 'validate'
        pos_hint: {'center_x': 0.5, 'center_y': 0.4}
        on_press: app.validator()
"""


class passwordvalidator(MDApp):
    def build(self):
        BuiltApp = Builder.load_string(app_Builder)
        return BuiltApp

    def validator(self):
        print('hello World')

passwordvalidator().run()
