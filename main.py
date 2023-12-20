import telebot
import datetime
import xml.etree.ElementTree as ET

from token_value import token
from src import def_lib as dl

bot = telebot.TeleBot(token)

date_format = '%Y-%m-%d'
lang = 'en'
c_lvl = 1

def main():
    
    global c_lvl

    @bot.message_handler(func=lambda message: message.text.startswith('/'))
    def start(msg) :
        n_item = dl.get_item(msg.text.lower())
        print(n_item)
        print_text = dl.print_menu_lvl(n_item)
        bot.send_message(msg.chat.id, print_text)


    bot.polling(none_stop = True)

if __name__ == '__main__':
    main()