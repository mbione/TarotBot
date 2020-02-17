import logging
import random
import telegram

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

updater = Updater("1034516978:AAHTZOJ39mZP7b8HEvjBNvVOP3Y4YBP0tHU", use_context=True)
bot = telegram.Bot(token="1034516978:AAHTZOJ39mZP7b8HEvjBNvVOP3Y4YBP0tHU")
# Get the dispatcher to register handlers
dp = updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

Arcanos = [
    ['https://raw.githubusercontent.com/mbione/TarotBot/master/img/major00_Easy-Resize.com.jpg', '00 - O louco'],
    ['https://raw.githubusercontent.com/mbione/TarotBot/master/img/major01_Easy-Resize.com.jpg', '01 - O Mago'], 
    ['https://raw.githubusercontent.com/mbione/TarotBot/master/img/major02_Easy-Resize.com.jpg', '02 - A Sacerdotisa'],
    ['https://raw.githubusercontent.com/mbione/TarotBot/master/img/major03_Easy-Resize.com.jpg', '03 - A Imperatriz'],
    ['https://raw.githubusercontent.com/mbione/TarotBot/master/img/major04_Easy-Resize.com.jpg', '04 - O Imperador'],
    ['https://raw.githubusercontent.com/mbione/TarotBot/master/img/major05_Easy-Resize.com.jpg', '05 - O Hierofante'],
    ['https://raw.githubusercontent.com/mbione/TarotBot/master/img/major06_Easy-Resize.com.jpg', '06 - Os Amantes'],
    ['https://raw.githubusercontent.com/mbione/TarotBot/master/img/major07_Easy-Resize.com.jpg', '07 - O Carro'],
    ['https://raw.githubusercontent.com/mbione/TarotBot/master/img/major08_Easy-Resize.com.jpg', '08 - A Força'],
    ['https://raw.githubusercontent.com/mbione/TarotBot/master/img/major09_Easy-Resize.com.jpg', '09 - O Eremita'],
    ['https://raw.githubusercontent.com/mbione/TarotBot/master/img/major10_Easy-Resize.com.jpg', '10 - A Roda da Fortuna'],
    ['https://raw.githubusercontent.com/mbione/TarotBot/master/img/major11_Easy-Resize.com.jpg', '11 - A Justiça'],
    ['https://raw.githubusercontent.com/mbione/TarotBot/master/img/major12_Easy-Resize.com.jpg', '12 - O Enforcado'],
    ['https://raw.githubusercontent.com/mbione/TarotBot/master/img/major13_Easy-Resize.com.jpg', '13 - A Morte'],
    ['https://raw.githubusercontent.com/mbione/TarotBot/master/img/major14_Easy-Resize.com.jpg', '14 - A Temperança'],
    ['https://raw.githubusercontent.com/mbione/TarotBot/master/img/major15_Easy-Resize.com.jpg', '15 - O Diabo'],
    ['https://raw.githubusercontent.com/mbione/TarotBot/master/img/major16_Easy-Resize.com.jpg', '16 - A Torre'],
    ['https://raw.githubusercontent.com/mbione/TarotBot/master/img/major17_Easy-Resize.com.jpg', '17 - A Estrela'],
    ['https://raw.githubusercontent.com/mbione/TarotBot/master/img/major18_Easy-Resize.com.jpg', '18 - A Lua'],
    ['https://raw.githubusercontent.com/mbione/TarotBot/master/img/major19_Easy-Resize.com.jpg', '19 - O Sol'],
    ['https://raw.githubusercontent.com/mbione/TarotBot/master/img/major20_Easy-Resize.com.jpg', '20 - O Julgamento'],
    ['https://raw.githubusercontent.com/mbione/TarotBot/master/img/major21_Easy-Resize.com.jpg', '21 - O Mundo']
    ]

def start(update, context):

    update.message.reply_text('Hi!')


def dia(update, context):

    random.shuffle(Arcanos)
    update.message.reply_text(Arcanos[0][1])
    #update.message.reply_text(Arcanos[0][0])
    #bot.sendPhoto(chat_id, Arcanos[0][0], Arcanos[0][1])
    chat_id = update.message.chat_id
    bot.sendPhoto(chat_id, Arcanos[0][0], Arcanos[0][1])


def error(update, context):

    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():

    #updater = Updater("1034516978:AAHTZOJ39mZP7b8HEvjBNvVOP3Y4YBP0tHU", use_context=True)
    #dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("dia", dia))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    updater.idle()


if __name__ == '__main__': 
    main()