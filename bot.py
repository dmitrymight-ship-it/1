import telebot
import os, random

# Замени 'TOKEN' на токен твоего бота
# Этот токен ты получаешь от BotFather, чтобы бот мог работать
bot = telebot.TeleBot("8561638027:AAF7NRMG_aE3Oryl3yAAIWXM1mauLy-4194")
text_messages = {
    "info": "My name is TeleBot,\n"
    "I am a bot that assists these wonderful bot-creating people of this bot library group chat.\n"
    "Also, I am still under development. Please improve my functionality by making a pull request! "
    "Suggestions are also welcome, just drop them in this group chat!",
    "wrong_chat": "Hi there!\nThanks for trying me out. However, this bot can only be used in the pyTelegramAPI group chat.\n"
    "Join us!\n\n"
    "https://telegram.me/joinchat/067e22c60035523fda8f6025ee87e30b",
}

@bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.reply_to(message, "Привет! Напиши своё имя.")

@bot.message_handler(func=lambda message: True)
def greeting_by_name(message):
    name = message.text
    response = (f"Привет, {name}!")
    bot.reply_to(message, response)



@bot.message_handler(commands=["hello"])
def send_hello(message):
    bot.reply_to(message, 'Привет! Как дела?')


@bot.message_handler(commands=["bye"])
def send_bye(message):
    bot.reply_to(message, 'Пока! Удачи!')

@bot.message_handler(commands=["info", "help"])
def on_info(message):
    bot.reply_to(message, text_messages["info"])


@bot.message_handler(commands=["heh"])
def send_heh(message):
    count_heh = int(message.text.split()[1]) if len(message.text.split()) > 1 else 5
    bot.reply_to(message, 'he' * count_heh)

@bot.message_handler(commands=['mem'])
def send_mem(message):
    img_name = random.choice(os.listdir("images"))
    with open(f'images/{img_name}', 'rb') as f:  
        bot.send_photo(message.chat.id, f)  

bot.polling()
