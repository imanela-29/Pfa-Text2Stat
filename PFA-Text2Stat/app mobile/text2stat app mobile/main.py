from kivymd.app import MDApp
from kivy.utils import platform
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivymd.theming import ThemableBehavior
from kivymd.uix.list import MDList
from kivymd.icon_definitions import md_icons
from kivymd.uix.list import OneLineIconListItem
from kivymd.uix.list import OneLineIconListItem
from kivy.uix.screenmanager import Screen
from kivy.app import App
from kivy.uix.label import Label

import os

from navigation_drawer import navigation_helper

Window.size = (500, 500)

class loginscreen (Screen):
    pass

class DemoApp(MDApp):
    class MyApp(App):
            def build(self):
                return Label(text='hello' )


    class ContentNavigationDrawer(BoxLayout):
        pass

    class DrawerList(ThemableBehavior, MDList):
        pass

    class loginscreen(Screen):
        pass

    def build(self):
        screen = Builder.load_string(navigation_helper)
        return screen

    def on_start(self):
        pass


DemoApp().run()