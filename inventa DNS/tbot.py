import telebot

bot = telebot.TeleBot('5592439647:AAEC-9hC_NT543FbY5ipHU-Kxf56XMkeOsY')


@bot.message_handler(commands=['start'])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Я на связи, напиши мне что-нибудь')


@bot.message_handler(content_types=['text'])
def handle_text(message):
    bot.send_message(message.chat.id, f'Вы написали: {message.text}')


bot.polling(none_stop=True, interval=0)
