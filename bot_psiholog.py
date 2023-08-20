import time

import telebot
import schedule
import datetime
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

bot = telebot.TeleBot('5930918805:AAE9VNBU3Q0LSYhrZ6rKs-4HjL5ZNOGtKJM')
activated_users = set()

@bot.message_handler(commands=['start'])
def welcome_message(message):
    chat_id = message.chat.id
    activated_users.add(chat_id)
    with open('welcome_picture.png', 'rb') as photo:
        with open('welcome_message.html', 'r', encoding='utf-8') as file:
            caption = file.read()
            keyboard = InlineKeyboardMarkup(row_width= 1)
            button1 = InlineKeyboardButton('ПОДПИСАТЬСЯ НА КАНАЛ', url='https://t.me/sistemansk')
            button2 = InlineKeyboardButton('ЭКСПРЕСС-ДИАГНОСТИКА ПОТЕНЦИАЛА стоимость 2500 рублей',
                                           callback_data='need_diagnostic')
            button3 = InlineKeyboardButton('ПРО ПРОГРАММУ АКТИВАЦИИ ПОТЕНЦИАЛА', callback_data='need_program')
            button4 = InlineKeyboardButton('УРОК "СТАНОВЛЕНИЕ ЭКСПЕРТА"', url='https://youtube.com')
            keyboard.add(button1, button2, button3, button4)
            bot.send_photo(chat_id, photo)
            bot.send_chat_action(chat_id, 'typing')
            time.sleep(2)
            bot.send_message(chat_id, text=caption, parse_mode='HTML')
            bot.send_chat_action(chat_id, 'typing')
            time.sleep(2)
            bot.send_message(chat_id, text=".", reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: call.data == 'need_diagnostic')
def handle_need_diagnostic_callback(call):
    user_chat_id = call.message.chat.id
    chat_id = call.message.chat.id
    activated_users.add(chat_id)
    user_name = call.from_user.first_name
    keyboard = InlineKeyboardMarkup(row_width=1)
    button5 = InlineKeyboardButton('Оплата из РФ', url='https://self.payanyway.ru/16881935468355')
    button6 = InlineKeyboardButton('Заполнить анкету',
                                   url='https://docs.google.com/forms/d/1AV0RrB8wysa7VYLiV0r_A_U8oNjgaW7ig3rreFn4YmA/edit')
    button7 = InlineKeyboardButton('Сообщить о проблемах с оплатой/анкетой', url='https://t.me/YanaRogozhnikova')
    keyboard.add(button5, button6, button7)
    bot.send_message('722847366', f'ЭКСПРЕСС-ДИАГНОСТИКА ПОТЕНЦИАЛА \n\nКонтакт пользователя: @{call.from_user.username}')
    bot.send_message(user_chat_id, 'Спасибо за интерес к диагностике❤️ \n\n<b>Для того, чтобы понять уровень использования вашего потенциала сейчас, я предлагаю заполнить анкету.</b> По результатам её заполнения, я запишу обратную <b>связь голосовым или текстовым сообщением</b> в ваш контакт в телеграмм. \n\n<b>Стоимость диагностики 2500 рублей.</b> \n\nОтвечайте так, как чувствуете на данный момент, здесь не важен анализ, а важны Ваши ощущения. \n\nСрок моего ответа обычно занимает 1-3 дня с момента оплаты и заполнения анкеты🌺 \n\nСОХРАНИТЕ, ПОЖАЛУЙСТА, ЧЕК ОБ ОПЛАТЕ', parse_mode='HTML', reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: call.data == 'need_program')
def handle_need_program_callback(call):
    chat_id = call.message.chat.id
    activated_users.add(chat_id)
    with open('lesson_picture.png', 'rb') as photo:
        user_chat_id = call.message.chat.id
        user_name = call.from_user.first_name
        keyboard = InlineKeyboardMarkup(row_width=1)
        button8 = InlineKeyboardButton('ЗАПОЛНИТЬ АНКЕТУ В ПРОГРАММУ',
                                       url='https://docs.google.com/forms/d/1qUoZyRtnJbsTSp3KGuDn8RvOK_3IEhwt8owRvVqRE2s/edit')
        button9 = InlineKeyboardButton('Сообщить о проблемах с анкетой', url='https://t.me/YanaRogozhnikova')
        keyboard.add(button8, button9)
        # bot.send_message('722847366', f'ПРОГРАММА АКТИВАЦИИ ПОТЕНЦИАЛА \n\nКонтакт пользователя: @{user_name}')
        bot.send_photo(user_chat_id, photo)
        bot.send_message(user_chat_id,
                         '&#10060;<b>Из точки непонимания куда двигаться дальше</b>,кем и с кем работать, кто мой клиент или работодатель и какой формат, отсутствия мотивации продолжать, сложного пути. \n\n&#9851;<b>К целостности, пониманию кто я, куда иду, разрешению себе быть сильным и работать с сильными</b>, <i>лёгкости, уверенности и истинной проявленности</i>. \n\n&#9745;<b>Формат</b> - индивидуальная работа, 2,5 мес (10 встреч) \n\nРезультат, как правило, у каждого свой и зависит от точки А и вашего запроса. Путь простраиваем индивидуально, с опорой на ключевые шаги \n\n<b>Максимально возможный результат</b>: \n\n&#128313;Сформируете видение своего будущего - образ с деталями, который работает как самосбывающееся пророчество, даёт мотивацию двигаться и преодолевать трудности, открывает путь \n\n&#128313;Расшифруете свою внутреннюю систему - уникальный способ создания всего, найдёте то, что даёт максимальный уровень энергии и самый быстрый результат \n\n&#128313;Поймёте вашу истинную силу, за что вам на самом деле платят \n\n&#128313;Получите состояние невероятной уверенности в себе и своём деле, заземлите все в понятной стратегии действий и сделаете первые шаги в моем сопровождении \n\n<b>Стоимость до конца августа</b> - 70 000 рублей',
                         parse_mode='HTML')
        bot.send_message(user_chat_id,
                         '<b>ПОНЯТЬ ПОДХОДИТ ЛИ ПРОГРАММА МОЖНО ЧЕРЕЗ ЗАПОЛНЕНИЕ АНКЕТЫ</b> \n\nЯ дам свою обратную связь поможет ли программа конкретно в вашем случае и какой потенциальный результат возможен \n\n<i>Заполните, пожалуйста, анкету в течение 48 часов</i> \n\nСрок моего ответа обычно занимает 1-3 дня',
                         parse_mode='HTML', reply_markup=keyboard)

bot.polling(none_stop=True, interval=0)
