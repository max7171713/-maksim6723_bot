import telebot
from telebot import types
token = "7487218942:AAG19VkhXheSjl_ULSC7EGj0f7Ns7YhtsV4"
bot=telebot.TeleBot(token)
@bot.message_handler(commands= ['start'])
def start(message):
    
    markup = types.ReplyKeyboardMarkup()
    button1 = types.KeyboardButton("нажми на меня")
    button2 = types.KeyboardButton("нажми")
    button3 = types.KeyboardButton("кот")
    markup.add(button1,button2,button3)
    bot.send_message(message.chat.id, 'привет',reply_markup=markup)
@bot.message_handler(commands= ['plus'])
def plus(message):
    markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton("няшка",callback_data = 'one')
    button2 = types.InlineKeyboardButton("котик",callback_data = 'to')
    markup.add(button1,button2)
    bot.send_message(message.chat.id, '+',reply_markup=markup)
    

@bot.callback_query_handler(func=lambda call:call.data)
def callback(call):
    if call.data == "to":
        bot.send_message(call.message.chat.id, 'да котики милые')





@bot.message_handler(content_types= ['text'])
def text(message):
    if message.text == "нажми на меня":
        bot.send_message(message.chat.id, 'ты взломон') 
    elif message.text == "нажми":
        bot.send_message(message.chat.id, 'тебе пополнено 1000 рублей')
    else:
        bot.send_message(message.chat.id, 'я вас не понимаю')


@bot.message_handler(content_types= ['photo'])
def photo(message):
    bot.reply_to(message, 'пшик')




@bot.message_handler(content_types= ['video'])
def video(message):
    bot.reply_to(message, 'пшик лол')






    
bot.polling()
