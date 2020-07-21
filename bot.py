from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from scraper import scraping
import logging
import os
import json
import requests

NAME = "lit-woodland-33204"
TOKEN = os.environ["TOKEN"]
PORT = os.environ.get("PORT", "5000")

updater = Updater(TOKEN)
dp = updater.dispatcher

def start(bot, update):
    reply = "Hello " + str(update.message.from_user.username) + "! \n The available functions are: \n /start to start the bot\n/tiles to see all tiles, or to find tiles by suits\n/rules for rules in Mahjong, including ways to win"
    bot.send_message(chat_id = update.message.chat_id, text=reply)

start_handler = CommandHandler('start', start)
dp.add_handler(start_handler)

# Other functions
def respond(bot, update):
    text = update.message.text

    if text == '/rules':
        reply = "In Mahjong, there are many ways to win. Some of the basic ones are: \
           1) Ping Hu\n \
           2) Peng Peng Hu\n \
           3) Qing Yi Se\n \
           4) Hun Yi Se \nWhich one do you want to know about?"

    bot.send_message(chat_id=update.message.chat_id, text=msg)

respond_handler = MessageHandler(Filters.text, respond)
dp.add_handler(respond_handler)
#     if "hate mahjong" in text:
#         reply = "Get out >:("
#     elif text == '/tiles':
#         reply = "Here is a list of all the tiles in Mahjong! Choose what *suit(e)s* your interest!"
#     #     status = requests.post("https://api.telegram.org/bot<" + TOKEN + ">/sendPhoto?chat_id=" + data['chat_id'], files=files)
#     # options = Telegram::Bot::Types::ReplyKeyboardMarkup
#     # .new(keyboard: [%w(Tong(dots) Tiao/Suo(bamboos)), %w(Wan(characters) DaPai(honours))], one_time_keyboard: true)
#     bot.api.send_message(chat_id=update.message.chat_id, text=reply, reply_markup=options)
# when 'Tong', 'Dots'
#     reply = "Here is a list of dotted tiles 筒子 in ascending order!"
#     #bot.api.send_photo(chat_id: message.chat.id, photo:
#      #   Faraday::UploadIO.new('/Users/mandy/Repos/MahjongMaster/photos/dots.jpg', 'image/jpeg'))
#     bot.api.send_message(chat_id: person_id, text: reply)
# when 'Tiao/Suo', 'Tiao', 'Suo', 'Bamboos'
#     reply = "Here is a list of bamboo tiles 条子/ 索子 in ascending order!"
#     #bot.api.send_photo(chat_id: message.chat.id, photo:
#      #   Faraday::UploadIO.new('/Users/mandy/Repos/MahjongMaster/photos/bamboos.jpg', 'image/jpeg'))
#     bot.api.send_message(chat_id: person_id, text: reply)
# when 'Wan', 'Characters'
#     reply = "Here is a list of character tiles 萬子 in ascending order!"
#     #bot.api.send_photo(chat_id: message.chat.id, photo:
#      #   Faraday::UploadIO.new('/Users/mandy/Repos/MahjongMaster/photos/characters.jpg', 'image/jpeg'))
#     bot.api.send_message(chat_id: person_id, text: reply)
# when 'DaPai', 'Honours'
#     reply = "Here is a list of honour tiles 大牌 in no particular order!"
#     #bot.api.send_photo(chat_id: message.chat.id, photo:
#      #   Faraday::UploadIO.new('/Users/mandy/Repos/MahjongMaster/photos/honours.jpg', 'image/jpeg'))
#     bot.api.send_message(chat_id: person_id, text: reply)
# when '/play'
#     reply = "Sorry I don't know how to play yet :/"
#     bot.api.send_message(chat_id: person_id, text: reply)
# when '/rules'
#     reply =
#     """
#     In Mahjong, there are many ways to win. Some of the basic ones are:
#     1) Ping Hu
#     2) Peng Peng Hu
#     3) Qing Yi Se
#     4) Hun Yi Se \nWhich one do you want to know about?
#     """
#     options = Telegram::Bot::Types::ReplyKeyboardMarkup
#     .new(keyboard: [%w(1 2), %w(3 4)], one_time_keyboard: true)
#     bot.api.send_message(chat_id: person_id, text: reply, reply_markup: options)
# else
#     reply = "I have no idea what #{command} means :("
#     bot.api.send_message(chat_id: person_id, text: reply)

# start webhooks
updater.start_webhook(listen="0.0.0.0",
        port=int(PORT),
        url_path=TOKEN)
updater.bot.setWebhook("https://{}.herokuapp.com/{}".format(NAME, TOKEN))
updater.idle()

print("sending '#{reply}' to @#{message.from.first_name}")

