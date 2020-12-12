#!/usr/bin/env python
# coding: utf-8

import telebot
import datetime

bot = telebot.TeleBot('1473868365:AAHkOU009n8mBC13B1Jl7R4NCSP4KVO81ng')


@bot.message_handler(content_types=["text"])
def handle_text_messages(message):
     if message.text == "/start":
        bot.send_message(message.from_user.id, "HoHoHo!")
        bot.send_message(message.from_user.id, "Привет! Я рада, что моя посылка дошла до тебя! Надеюсь она сделает твои новогодние праздники чуть теплее.")
        bot.send_animation(message.from_user.id, r'https://i.ibb.co/YNLVMFJ/With-love-Mrs-Santa-Claus.gif') #приветствие
        
        keyboard = telebot.types.InlineKeyboardMarkup()
        key_dalee = telebot.types.InlineKeyboardButton(text='Далее', callback_data='next')
        keyboard.add(key_dalee)
        bot.send_message(message.from_user.id, text = 'Для продолжения нажми "Далее"', reply_markup=keyboard)

        @bot.callback_query_handler(func=lambda call: True)
        def callback_worker(call): 
            if call.data == "next":
                bot.send_photo(message.from_user.id, r'https://i.ibb.co/6sC5MQz/Kopia-With-love-Mrs-Santa-Claus.gif') #активируй магию
                keyboard = telebot.types.InlineKeyboardMarkup()
                key_active = telebot.types.InlineKeyboardButton(text='Магия активирована!', callback_data='active')
                keyboard.add(key_active)
                bot.send_message(message.from_user.id, text = 'Когда будешь готова - нажимай кнопку.', reply_markup=keyboard)
            elif call.data == 'active':
                bot.send_message(message.from_user.id, text = 'Давай применим твой подарок по назначению!')
                bot.send_photo(message.from_user.id, r'https://i.ibb.co/Tk5Z5By/With-love-Mrs-Santa-Claus-kopia-2.gif') #step 2
                
                keyboard = telebot.types.InlineKeyboardMarkup()
                key_recept_1 = telebot.types.InlineKeyboardButton(text='Ленивые будни', callback_data='lazy')
                keyboard.add(key_recept_1)
                key_recept_2 = telebot.types.InlineKeyboardButton(text='Наедине с собой', callback_data='scandy')
                keyboard.add(key_recept_2)
                key_recept_3 = telebot.types.InlineKeyboardButton(text='Классический ужин', callback_data='classic')
                keyboard.add(key_recept_3)
                bot.send_message(message.from_user.id, text = 'Сделай свой выбор', reply_markup=keyboard)
            elif call.data == 'lazy':
                bot.send_photo(message.from_user.id, r'https://i.ibb.co/ScYKgJB/With-love-Mrs-Santa-Claus-kopia-3.gif')
                now = datetime.datetime.now()
                then = datetime.datetime(2021, 1, 1) 
                delta = then - now
                bot.send_message(message.from_user.id, text = 'Отличного вечера и весёлых каникул!')
                bot.send_message(message.from_user.id, text = 'До Нового года осталось ' + str(delta.days) + ' дней:)')
            elif call.data == 'scandy':
                bot.send_photo(message.from_user.id, r'https://i.ibb.co/x7VdnQg/With-love-Mrs-Santa-Claus-kopia-5.gif')
                now = datetime.datetime.now()
                then = datetime.datetime(2021, 1, 1) 
                delta = then - now
                bot.send_message(message.from_user.id, text = 'Отличного вечера и весёлых каникул!')
                bot.send_message(message.from_user.id, text = 'До Нового года осталось ' + str(delta.days) + ' дней:)')
            elif call.data == 'classic':
                bot.send_photo(message.from_user.id, r'https://i.ibb.co/G0VwS5B/With-love-Mrs-Santa-Claus-kopia-4.gif')
                now = datetime.datetime.now()
                then = datetime.datetime(2021, 1, 1) 
                delta = then - now
                bot.send_message(message.from_user.id, text = 'Отличного вечера и весёлых каникул!')
                bot.send_message(message.from_user.id, text = 'До Нового года осталось ' + str(delta.days) + ' дней:)')
                            
if __name__ == '__main__':
    bot.polling(none_stop=True)




