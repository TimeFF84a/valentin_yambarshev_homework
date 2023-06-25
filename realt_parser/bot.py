import telebot
import parser
from apartment import Apartment
from telebot.types import ReplyKeyboardMarkup

bot = telebot.TeleBot('6248078020:AAFef3t-XtDdVXikd1OQsyvUyO6a1_Xe2-I')


@bot.message_handler()
def parse(message):
    if message.text == '/start':
        menu = ReplyKeyboardMarkup(resize_keyboard=True)
        menu.row('Добавить квартиру в отслеживание', 'Включить режим отслеживания')
        bot.send_message(message.chat.id, 'Привет, это бот для парсинга данных с realt.by', reply_markup=menu)


bot.polling()
