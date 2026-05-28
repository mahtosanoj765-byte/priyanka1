import telebot
import google.generativeai as genai
import os

TOKEN = "8707525218:AAGydKx1TnX2YIXZ1R_x1MbOwB4LSXADbw8"
genai.configure(api_key="AIzaSyCBB3ED9IgsmShKerZTRATTW7urGkD2cXc")

model = genai.GenerativeModel("gemini-1.5-flash")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func=lambda message: True)
def echo(message):
    response = model.generate_content(message.text)
    bot.reply_to(message, response.text)

bot.infinity_polling()
