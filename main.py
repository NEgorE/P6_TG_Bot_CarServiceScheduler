import telebot
import datetime
import xml.etree.ElementTree as ET


from token_value import token
from src import def_lib as dl
from src.db import db_sqla as dbc


bot = telebot.TeleBot(token)

date_format = '%Y-%m-%d'
lang = 'en'

def main():

    dbc.db_init()

    @bot.message_handler(commands=["start"])
    def start(msg) :
        print(msg.from_user.id, msg.from_user.username, msg.from_user.first_name, msg.from_user.last_name, msg.from_user.language_code)
        dbc.sb_session_open()
        if dbc.session.query(dbc.User).filter(dbc.User.tg_id == msg.from_user.id).count() < 1 :
            new_user = dbc.new_user(msg.from_user.id, msg.from_user.username, msg.from_user.first_name, msg.from_user.last_name, msg.from_user.language_code)
            dbc.session.add(new_user)
            dbc.session.commit()
            dbc.session.close()
        else :    
            bot.send_message(msg.chat.id, msg_txt_lib['hi_str_1'])
            dbc.session.close()

    @bot.message_handler(func=lambda message: message.text.startswith('/'))
    def anycommand(msg) :
        print(msg.from_user.id, msg.from_user.username, msg.from_user.first_name, msg.from_user.last_name, msg.from_user.language_code)
        n_item = dl.get_item(msg.text.lower())
        print(n_item)
        print_text = dl.print_menu_lvl(n_item, lang)
        bot.send_message(msg.chat.id, print_text)


    bot.polling(none_stop = True)

if __name__ == '__main__':
    main()