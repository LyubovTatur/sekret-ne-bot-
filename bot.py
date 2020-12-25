import telebot
import config
import random

bot = telebot.TeleBot(config.TOKEN)
random_cute_massage = None
@bot.message_handler(content_types=['text'])
def mirror(message):
    random_cute_massage = config.CUTE_MESSAGES[random.randint(0,len(config.CUTE_MESSAGES))-1]
    bot.send_message(message.chat.id, random_cute_massage)

bot.polling(none_stop = True)
