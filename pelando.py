import kivy
import requests





kivy.require('1.9.0')

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout


class PelandoNotifier(App):
	def build(self):
		self.window = GridLayout()
		self.window.cols = 2

		self.label = Label(text="CONTENT")
		self.window.add_widget(self.label)
		self.button = Button(text="Get RSS")
		self.window.add_widget(self.button)
		self.button.bind(on_press=self.getRSS)


		return self.window


	def getRSS(self, instance):
		self.label.text = "RESULTADOS RSS PELANDO: 1. CADEIRA GAMER"


pelandoApp = PelandoNotifier()
pelandoApp.run()


