from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivy.lang import Builder
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton

username_helper = """
MDTextField:
    hint_text: "Enter username"
    pos_hint: {'center_x': 0.5, 'center_y': 0.6}
    size_hint_x: 0.7
    icon_left: "account-circle"
    icon_left_color: app.theme_cls.primary_color
    helper_text: "enter username correctle"
    helper_text_mode: "on_focus"
"""
password_helper = """
MDTextField:
    hint_text: "Enter password"
    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
    size_hint_x: 0.7
    icon_left: "lock"
    icon_left_color: app.theme_cls.primary_color
    helper_text: "enter password correctly"
    helper_text_mode: "on_focus"
"""

class DemoApp(MDApp):
    def build(self):
        screen = Screen()
        self.theme_cls.primary_palette = "Blue"
        self.username = Builder.load_string(username_helper)
        self.password = Builder.load_string(password_helper)
        button1 = MDRectangleFlatButton(
            text = "LogIn",
            pos_hint = {'center_x': 0.5, 'center_y': 0.4},
            size_hint_x = None,
            width = 150,
            on_release = self.on_login
        )

        screen.add_widget(self.username)
        screen.add_widget(self.password)
        screen.add_widget(button1)

        return screen

    def on_login(self, obj):
        close_button = MDFlatButton(text="Close", on_release=self.close_diag)
        self.dialog = MDDialog(
            title = "Information!",
            text = "created by Mayur Solanki",
            size_hint_x = 0.7,
            buttons = [close_button]
        )
        self.dialog.open()

    def close_diag(self, obj):
        self.dialog.dismiss()



DemoApp().run()