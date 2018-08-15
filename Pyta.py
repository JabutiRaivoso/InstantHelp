import kivy
import mysql.connector
kivy.require('1.7.0')


from kivy.app import App, runTouchApp
from kivy.uix.image import Image
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.graphics import BorderImage
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.screenmanager import Screen
from kivy.config import Config
from kivy.uix.screenmanager import RiseInTransition
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.uix.popup import Popup

Config.set('graphics', 'width', '300')
Config.set('graphics', 'height', '200')


cnx = mysql.connector.connect(user='root',password='',host='localhost',database='instanthelp')
cursor = cnx.cursor()

class TelaLogin(Screen):
    def pegad(self):
        user = self.ids.usuario.text
        passw = self.ids.senha.text

        query = ("select NomeUsuario from usuario where NomeUsuario= %s and SenhaUsuario= %s")
        cursor.execute(query,(user,passw,))
        nme=cursor.fetchone()
        print(nme)

        if nme==None:
            popup= Popup(title='Erro!',content=Label(text='Usuario ou senha incoretos!'),size_hint=(None, None), size=(400, 200))
            popup.open()
        else:
            self.ids.teste.text='USUÁRIO CORRETO! Conectando..'
            self.manager.current='Tmenu'

class TelaCadas(Screen):
    def voltal(self):
        self.manager.current='Tlogin'

    def Icadas(self):
        user=self.ids.usuario
        passw=self.ids.senha
        idade=self.ids.idade
        email=self.ids.email





class MenuPrin(Screen):
    pass

class manager(ScreenManager):
    pass

manager.transition = RiseInTransition()

class Pyta(App):

    def build(self):
        self.title='Instant Help'
        self.icon='icob.png'
        return manager()

Pyta().run()
