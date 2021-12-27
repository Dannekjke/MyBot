
import telebot

from telebot import types
bot = telebot.TeleBot('Token')
@bot.message_handler(commands=['start'])
def welcome(message):
    sti = open('static/welcome.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)
    markup= types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Петух")
    item2 = types.KeyboardButton("Кабан")
    item3 = types.KeyboardButton("Конь")
 
    markup.add(item1, item2, item3)
 
    bot.send_message(message.chat.id, "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, И у меня есть для тебя подрок! Ответь на один вопрос: Какое у Лехи любимое животное".format(message.from_user, bot.get_me()),
        parse_mode='html', reply_markup=markup)
@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == 'private':
        if message.text == 'Кабан':
            bot.send_message(message.chat.id, 'Не верно')

        elif message.text == "Петух":
            bot.send_message(message.chat.id, "Здесь будет подрок")

        elif message.text == "Кабан":
            bot.send_message(message.chat.id, 'Не верно')

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="",
                reply_markup=None)
 
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                text="")
 
    except Exception as e:
        print(repr(e))
 
bot.polling(none_stop=True)
