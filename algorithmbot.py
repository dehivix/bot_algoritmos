# -*- coding: utf-8 -*-
import django
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bot_algoritmos.settings")
django.setup()
import sys
import requests
from django.contrib import admin
from estudiantes.models import Estudiantes
from notas.models import Cohorte
from notas.models import PlanEvaluacion
from notas.models import Periodo
from notas.models import Notas
import telebot
import time

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


#Mensaje para datos
@bot.message_handler(commands=['datos'])
def send_info(message):
    cedula = message.text.strip('/datos').lstrip(' ').replace(' ', '_')
    try:
        estudiante = Estudiantes.objects.get(cedula=cedula)
    except:
        estudiante = 'LA CEDULA PROPORCIONADA ES INCORRECTA.'

    bot.reply_to(message, """\
    Sus datos son:  """+str(estudiante)+"""\
    """)


#mensaje para notas
@bot.message_handler(commands=['notas'])
def send_notas(message):
    salida = ''
    estudiante = ''
    notas_concat = ''
    cedula = message.text.strip('/notas').lstrip(' ').replace(' ', '_')
    notas = Notas.objects.filter(estudiante__cedula=cedula)
    #import ipdb;ipdb.set_trace()
    if notas.exists():
        estudiante = str(notas[0].estudiante)+'->'
        for nota in notas:
            cohorte = str(nota.actividad.cohorte.nombre)+' cohorte: '
            actividad = nota.actividad.actividad+'--nota: '
            nota_actual = nota.nota
            notas_concat += cohorte+actividad+nota_actual+' '
        salida = notas_concat
    else:
        salida = 'LA CEDULA PROPORCIONADA ES INCORRECTA O NO POSEE NOTAS TODAVIA.'

    bot.reply_to(message, """\
    """+estudiante+"""Sus Notas son:  """+salida+"""\
    """)

#Mensaje de despedida
@bot.message_handler(commands=['chao'])
def send_siao(message):
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


while True:
    try:
        bot.polling(none_stop=True)
    except requests.exceptions.ConnectionError as e:
        print >> sys.stderr, str(e)
        time.sleep(15)
