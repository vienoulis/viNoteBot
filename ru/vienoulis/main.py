import telebot

bot = telebot.TeleBot('855393784:AAGxBrLMZoVjzcWv6veIh2YyhQdt5UmfX6o')


@bot.message_handler(content_types=['text'])
def start(msg):
    bot.send_message(msg.chat.id, 'Hello world')


bot.polling(none_stop=True)
