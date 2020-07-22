import requests
import os
import sys

class ConvertText(object):
	"""docstring for ConvertText"""
	def __init__(self):
		super(ConvertText, self).__init__()
		self.enc = ""
		self.text = ""
		self.lang = ""
		self.speed = ""
		url = ""
		
	def set_encoding(self):
		try:
			self.enc = input("Type your character encoding(such as: UTF-8,ANSI,Windows-1254,ASCII): ")
			if self.enc in ["UTF-8","ANSI","Windows-1254","ASCII"]:
				return self.enc
		except:
			return "UTF-8"

	def set_text(self):
		try:
			self.text = input("Type what you want to convert text to speech: ")
			if self.text:
				return self.text
		except:
			return "Hello World"

	def set_lang(self):
		try:
			self.lang = input("Type lang(such as 'en' or 'tr')             : ")
			if self.lang in ["en","tr"]:
				return self.lang
		except:
			return "en"

	def set_speed(self):
		try:
			self.speed = float(input("Set speed of voice (between 0.1 - 1.0) : "))
			if self.speed in range(0.1,1.0):
				return str(self.speed)
		except:
			return "0.8"

	def downloadVoice(self):
		self.enc = self.set_encoding()
		self.text = self.set_text()
		self.lang = self.set_lang()
		self.speed = self.set_speed()
		filename = self.text[:5] + ".mp3"
		url = f"""https://translate.google.com/translate_tts?ie={self.enc}&q={self.text}&tl={self.lang}&ttsspeed={self.speed}&total=1&idx=1&client=tw-ob&textlen={len(self.text)}"""

		r = requests.get(url,stream=True)
		with open(filename,"wb") as f:
			f.write(r.content)
try:
	ct = ConvertText()
	ct.downloadVoice()
except Exception as e:
	print(e)
