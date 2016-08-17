# coding: utf-8
"""
    Test application for VK API usages
"""
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget
from vk_api import *

__version__ = '1.0'


main_widget = """
<MainWidget>:
    BoxLayout:
        id: control_panel
        orientation: 'vertical'
        size_hint: 1, 1
        size: root.width, root.height

        Button:
            id: login_button
            size_hint: 1, None
            size: root.width, '40dp'
            text: 'VK login'
            on_press: root.login()

        Button:
            id: join_button
            size_hint: 1, None
            size: root.width, '40dp'
            text: 'VK join group'
            on_press: root.join()
"""

Builder.load_string(main_widget)


class MainWidget(Widget):
    def __init__(self, *args, **kwargs):
        super(MainWidget, self).__init__(*args, **kwargs)
        vk = VkIosApi()
        vk.use()
        # vk.auth()

    def login(self):
        vk = VkIosApi()
        vk.auth()


if __name__ == '__main__':
    class MainApp(App):
        def on_pause(self):
            return True

        def build(self):
            return MainWidget()


    MainApp().run()
