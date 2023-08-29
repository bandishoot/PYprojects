import telebot as t

bot = t.TeleBot('6286112869:AAFEpL9dSPkjzR2mBgzZsM5CMkffuLWPl5A')

@bot.message_handlers(commands=['start'])
def start(message):
     bot.send_message()

