import telebot
from gtts import gTTS
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import os

bot = telebot.TeleBot('TOKEN')
vol = ''



keyboard1 = telebot.types.ReplyKeyboardMarkup(True, True, True, True)
keyboard1.row('/voices')


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Выбери действие', reply_markup=keyboard1)

@bot.message_handler(commands=['voices'])
def add_new(message):
    bot.send_message(message.chat.id, 'Введите строку')
    bot.register_next_step_handler(message, voices)

def voices(message):
    vol = str(message.text)
    print(vol)
    requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
    tts = gTTS(vol, lang='ru')
    tts.save('h.mp3')
    bot.send_voice(message.chat.id, open('h.mp3', 'rb'))
    os.remove('h.mp3')

bot.polling()
