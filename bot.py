from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
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

# Other commands

def rules(bot, update):
    reply = "In Mahjong, there are many ways to win. Some of the basic ones are: \n \
               1) Ping Hu\n \
               2) Peng Peng Hu\n \
               3) Qing Yi Se\n \
               4) Hun Yi Se \nWhich one do you want to know about?"
    bot.send_message(chat_id=update.message.chat_id, text=reply)

rules_handler = CommandHandler('rules', rules)
dp.add_handler(rules_handler)

def win(bot, update):
    reply = "Here are 4 main ways to win in Mahjong, which would you like to know about?"

    bot.send_message(chat_id=update.message.chat_id, text=reply)

    # keyboard = [
    #     [ InlineKeyboardButton("Ping Hu"), InlineKeyboardButton("Peng Peng Hu") ],
    #     [ InlineKeyboardButton("Qing Yi Se"), InlineKeyboardButton("Hun Yi Se") ]
    # ]
    # reply_markup = InlineKeyboardMarkup(keyboard)
    # bot.send_message(chat_id=update.message.chat_id, text=reply, reply_markup=reply_markup)

win_handler = CommandHandler('win', win)
dp.add_handler(win_handler)

def tiles(bot, update):
    reply = "Here is a list of all the tiles in Mahjong! Choose what *suit(e)s* your interest!"
    bot.send_message(chat_id=update.message.chat_id, text=reply)
    bot.send_photo(chat_id=update.message.chat_id, photo="https://raw.githubusercontent.com/tirameshu/MahjongMaster/master/photos/tiles.jpg")

# normal functions
def ping_hu_reply(bot, chat_id):
    bot.send_photo(chat_id=chat_id, photo="https://raw.githubusercontent.com/tirameshu/Mahjong_Master_python/master/photos/pinghu.png")
    reply = "Above is an example of the Ping Hu (平胡) hand.\n \
    Requirements:\n \
    1) No honour tiles that can give multipliers\n \
    2) No triplets (all sets must be sequential)\n \
    3) Waiting hand must be able to win with **at least** 2 different tiles\n \
    The hand below is not Ping Hu:"
    bot.send_photo(chat_id=chat_id, photo="https://raw.githubusercontent.com/tirameshu/Mahjong_Master_python/master/photos/not%20pinghu.png")
    return reply

def pengpenghu_reply(bot, chat_id):
    bot.send_photo(chat_id=chat_id, photo="https://raw.githubusercontent.com/tirameshu/Mahjong_Master_python/master/photos/pinghu.png")
    reply = "Above is an example of the Ping Hu (平胡) hand.\n \
    Requirements:\n \
    1) No honour tiles that can give multipliers\n \
    2) No triplets (all sets must be sequential)\n \
    3) Waiting hand must be able to win with **at least** 2 different tiles\n \
    The hand below is not Ping Hu:"
    bot.send_photo(chat_id=chat_id, photo="https://raw.githubusercontent.com/tirameshu/Mahjong_Master_python/master/photos/not%20pinghu.png")
    return reply

tiles_handler = CommandHandler('tiles', tiles)
dp.add_handler(tiles_handler)

# General text responses
def respond(bot, update):
    text = update.message.text
    chat_id = update.message.chat_id

    if text.lower() == "ping hu":
        reply = ping_hu_reply(bot, chat_id)
    else:
        reply = "Sorry! I can't really converse yet :("

    bot.send_message(chat_id=chat_id, text=reply)

respond_handler = MessageHandler(Filters.text, respond)
dp.add_handler(respond_handler)

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
