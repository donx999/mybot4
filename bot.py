import telebot

# Tokeningizni shu yerga yozing
TOKEN = "8391309835:AAEpzJS9M3aJCxffYCIwQs4EIeKCzTzOmwM"

bot = telebot.TeleBot(TOKEN)

# /start buyrug‘i uchun javob
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(
        message,
        "Assalomu alaykum!\n"
        "Angor tumanidagi 9-maktab test botiga xush kelibsiz!\n"
        "Bot manzilingiz: @uzbgetest_bot"
    )

# Oddiy yozilgan xabarlarga javob
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, f"Siz yozdingiz: {message.text}")

print("Bot ishlamoqda...")
bot.infinity_polling()
