import telebot
import google.generativeai as genai
import os

TOKEN = "8771761481:AAF5i8894_QAa5V7_dAkcUpqci8d8wEogss"
genai.configure(api_key="AIzaSyCBB3ED9IgsmShKerZTRATTW7urGkD2cXc")

model = genai.GenerativeModel("gemini-1.5-flash")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func=lambda message: True)
def echo(message):
    response = model.generate_content(message.text)
    bot.reply_to(message, response.text)

bot.infinity_polling()
