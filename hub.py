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
    bot.reply_to(message,f"{message.chat.id}")
    bot.send_message(message.chat.id, 'привет',reply_markup=markup)
    
    
@bot.message_handler(commands= ['plus'])
def plus(message):
    markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton("няшка",callback_data = 'one')
    button2 = types.InlineKeyboardButton("котик",callback_data = 'to')
    button3 = types.InlineKeyboardButton("видео",callback_data = 'iu')
    button4 = types.InlineKeyboardButton("gif",callback_data = 'git')
    button5 = types.InlineKeyboardButton("мяу",callback_data = 'mur')
    button6 = types.InlineKeyboardButton("cashback",callback_data = 'r')
    markup.add(button1,button2,button3,button4,button5,button6)
    bot.send_message(message.chat.id, '+',reply_markup=markup)
    

@bot.callback_query_handler(func=lambda call:call.data)
def callback(call):
    if call.data == "to":
        bot.send_message(call.message.chat.id, 'да котики милые')
        
    if call.data == "one":
        photo = open('котик.jpg','rb')
        bot.send_photo(call.message.chat.id, photo)

    if call.data == "iu":
        video = open('sbezhal-ot-poceluev.mp4','rb')
        bot.send_video(call.message.chat.id, video)
        
    if call.data == "git":
        animation = open('git.gif','rb')
        bot.send_animation(call.message.chat.id, animation)
        
    if call.data == "mur":
        audio = open('kot_-_myaukane.mp3','rb')
        bot.send_audio(call.message.chat.id, audio)

    if call.data == "r":
        video = open('kot-fleksit-pod-kesbek-na-vse_(videomega.ru).mp4','rb')
        bot.send_video(call.message.chat.id, video)




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

