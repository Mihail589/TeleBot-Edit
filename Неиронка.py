import telebot
import os
from random import randint
import time
from evaluate import main
from utils import list_files
import sys
import requests
from youtubesearchpython import VideosSearch 

t = "6074293789:AAHTiCZU6mAnXBJmE0qnHfnaCXHVwz2n6Hg"
bot = telebot.TeleBot(t)
if not os.path.exists("in"):
	os.mkdir('in')
if not os.path.exists("out"):
	os.mkdir('out')
@bot.message_handler(commands= ['start'])
def Hey(message):
	bot.send_message(message.chat.id, f"Привет {message.chat.username}.")
	bot.send_message(message.chat.id, f"Скинь мне фотку а я наложу на неё некоторые эфекты.")
	bot.send_message(message.chat.id, f"Также напиши /Pogoda далее город и ты получишь погоду в выбранно городе.")
	bot.send_message(message.chat.id, f"Также напиши /vidos и + тему я тебя скину самое лучшее видео на ютубе по выбранной теме.")
@bot.message_handler(content_types = ['photo'])
def hello(message):
	a=1
	namein = str(randint(10**6, 10**8))
	fileID = message.photo[-1].file_id
	file_info = bot.get_file(fileID)
	filed = bot.download_file(file_info.file_path)
	with open(f"in/{namein}.jpg", "wb") as file:
		file.write(filed)
	for ckpt in list_files('ckpt'):
		nameout = str(randint(10**6, 10**8))
		model = os.path.abspath('ckpt/' + ckpt)
		print(a)
		main(model, "in", "out")
		os.rename(f"out/{namein}.jpg", f"out/{nameout}.jpg")
		with open(f"out/{nameout}.jpg", "rb") as file:
			bot.send_photo(message.chat.id, file)
		a+=1
	os.remove(f"in/{namein}.jpg")
@bot.message_handler(func=lambda message: True) 
def echo_all(message):
	print(message.text)
	if "pogoda" in message.text:
		text =  message.text.split()
		print(text)
		wether = {
			'format': 2,
			'lang': "ru",
			'M': ''
		}
		bot.send_message(message.from_user.id, requests.get(f"https://wttr.in/{text[1]}", params = wether).text)
	elif "vidos" in message.text:
		text =  message.text.split()
		link = VideosSearch(text[1], limit=1).result()["result"][0]['link']
		bot.send_message(message.chat.id, link)
	else:
		print("a")
#bot.polling(none_stop = True)

while True:
	try:
		bot.polling(none_stop = False)
	except:
		print("ОШИБКА 606")
	time.sleep(3)