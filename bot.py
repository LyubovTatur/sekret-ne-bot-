import telebot
import config
import random

from telebot import types

bot = telebot.TeleBot(config.TOKEN)
random_cute_massage = None
@bot.message_handler(commands=['start'])
def welcome(message):
    pic = open('pics//neco_girls.jpg','rb')
    bot.send_photo(message.chat.id, pic)
    bot.send_message(message.chat.id,'приветки {0.first_name}ка'.format(message.from_user))


@bot.message_handler(content_types=['text'])
def mirror(message):
    random_cute_massage = config.CUTE_MESSAGES[random.randint(0,len(config.CUTE_MESSAGES))-1]
    bot.send_message(message.chat.id, random_cute_massage)

bot.polling(none_stop = True)
