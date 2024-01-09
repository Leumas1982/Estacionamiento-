import kivy
import kivymd



from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition



from kivymd.app import MDApp
from kivymd.theming import ThemableBehavior
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDTextButton, MDFillRoundFlatButton
from kivymd.uix.list import MDList

Window.size = (600, 800)

Builder.load_file('kvs\login.kv')
Builder.load_file('kvs\main.kv')
Builder.load_file('kvs\Basica.kv')
Builder.load_file('kvs\contacto.kv')
Builder.load_file('kvs\placas.kv')
Builder.load_file('kvs\modelo.kv ')
Builder.load_file('kvs\Fila.kv')

class WindowManager(ScreenManager):
    pass
class LoginScreen(Screen):
    pass
class MainScreen(Screen):
    pass
class BasicaScreen(Screen):
    pass
class ContactoScreen(Screen):
    pass
class PlacasScreen(Screen):
    pass
class ModeloScreen(Screen):
    pass 
class FilaScreen(Screen):
    pass



class MainApp(MDApp):
    def __init__(self, **kwargs):
        self.title = "Estacionamiento CUCEI"
        super().__init__(**kwargs)
    def build(self):
        self.wm = WindowManager()
        screens = [
            LoginScreen(name='login'),
            MainScreen(name='main'),
            BasicaScreen(name='Basica'),
            ContactoScreen(name='contacto'),
            PlacasScreen(name='placas'),
            ModeloScreen(name='modelo'),
            FilaScreen(name='fila')
        ]
        for screen in screens:
            self.wm.add_widget(screen)
        return self.wm


if __name__ == '__main__':
    MainApp().run()