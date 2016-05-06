# -*- coding: utf-8 -*-
import os
import sys
import requests

#os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bot_algoritmos.settings")
#from django.contrib import admin
#from bot.models import *
#from wiki import wiki
#from google import google
import telebot

#Llamado al bot desde la api de telegram
API_TOKEN = '138678282:AAEHgnAE5QBluRPnOurYV2hm5SdwEjFjXxI'
bot = telebot.TeleBot(API_TOKEN)

#Mensaje de inicio
@bot.message_handler(commands=['start', 'hola'])
def send_welcome(message):
    try:
        user = message.from_user.username
    except:
        user = ''
    bot.reply_to(message, """\
    Hola @"""+user+"""\
    Espero que te encuentres bien, soy un bot creado con la intencion de asistir\
    en labores pertinentes a la asignatura! Gusto en saludarte.\
    Creado por @dehivix
    """)
'''
#Busquedas en wikipedia
@bot.message_handler(commands=['wiki'])
def BuscarWiki(message):
    respuesta=wiki(message)
    if ("Cannot acces link!" in respuesta):
        reply="No hay articulos en wikipedia\n"
    bot.reply_to(message, respuesta)
#Busquedas en google
@bot.message_handler(commands=['google'])
def BuscarGoogle(message):
    respuesta=google(message)
    bot.reply_to(message, respuesta)
'''

#Mensaje de despedida
@bot.message_handler(commands=['chao'])
def send_welcome(message):
    user = message.from_user.username
    bot.reply_to(message, """\
    Vete tu!!! Yo llegue primero...\
    """)
#Texto por defecto
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, """\
    Lo siento, soy un bot, solo estoy programado para responder algunos comandos.\
    """)

#bot.polling()

while True:
    try:
        bot.polling(none_stop=True)
    except requests.exceptions.ConnectionError as e:
        print >> sys.stderr, str(e)
        time.sleep(15)
