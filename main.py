import logging
import random
import telegram
import numpy as np

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

updater = Updater("1034516978:AAHTZOJ39mZP7b8HEvjBNvVOP3Y4YBP0tHU", use_context=True)
bot = telegram.Bot(token="1034516978:AAHTZOJ39mZP7b8HEvjBNvVOP3Y4YBP0tHU")
# Get the dispatcher to register handlers
dp = updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)
AsPaus = ''
DoisPaus = ''
TresPaus = ''
QuatroPaus = ''
CincoPaus = ''
SeisPaus = ''
SetePaus = ''
OitoPaus = ''
NovePaus = ''
DezPaus = ''
PagePaus = ''
CavaleiroPaus = ''
RainhaPaus = ''
ReiPaus = ''
AsCopas = ''
DoisCopas = ''
TresCopas = ''
QuatroCopas = ''
CincoCopas = ''
SeisCopas = ''
SeteCopas = ''
OitoCopas = ''
NoveCopas = ''
DezCopas = ''
PageCopas = ''
CavaleiroCopas = ''
RainhaCopas = ''
ReiCopas = ''
AsEspadas = ''
DoisEspadas = ''
TresEspadas = ''
QuatroEspadas = ''
CincoEspadas = ''
SeisEspadas = ''
SeteEspadas = ''
OitoEspadas = ''
NoveEspadas = ''
DezEspadas = ''
PageEspadas = ''
CavaleiroEspadas = ''
RainhaEspadas = ''
ReiEspadas = ''
AsMoedas = ''
DoisMoedas = ''
TresMoedas = ''
QuatroMoedas = ''
CincoMoedas = ''
SeisMoedas = ''
SeteMoedas = ''
OitoMoedas = ''
NoveMoedas = ''
DezMoedas = ''
PageMoedas = ''
CavaleiroMoedas = ''
RainhaMoedas = ''
ReiMoedas = ''


ArcanosMaiores = [
    ['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite00.jpg', '00 - O louco'],
    ['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite01.jpg', '01 - O Mago'], 
    ['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite02.jpg', '02 - A Sacerdotisa'],
    ['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite03.jpg', '03 - A Imperatriz'],
    ['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite04.jpg', '04 - O Imperador'],
    ['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite05.jpg', '05 - O Hierofante'],
    ['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite06.jpg', '06 - Os Amantes'],
    ['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite07.jpg', '07 - O Carro'],
    ['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite08.jpg', '08 - A Força'],
    ['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite09.jpg', '09 - O Eremita'],
    ['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite10.jpg', '10 - A Roda da Fortuna'],
    ['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite11.jpg', '11 - A Justiça'],
    ['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite12.jpg', '12 - O Enforcado'],
    ['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite13.jpg', '13 - A Morte'],
    ['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite14.jpg', '14 - A Temperança'],
    ['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite15.jpg', '15 - O Diabo'],
    ['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite16.jpg', '16 - A Torre'],
    ['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite17.jpg', '17 - A Estrela'],
    ['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite18.jpg', '18 - A Lua'],
    ['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite19.jpg', '19 - O Sol'],
    ['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite20.jpg', '20 - O Julgamento'],
    ['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite21.jpg', '21 - O Mundo']
    ]
ArcanosMenores = [
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite22.jpg', 'Ás de Paus'],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite23.jpg', '2 de Paus'],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite24.jpg', '3 de Paus'],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite25.jpg', '4 de Paus'],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite26.jpg', '5 de Paus'],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite27.jpg', '6 de Paus'],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite28.jpg', '7 de Paus'],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite29.jpg', '8 de Paus'],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite30.jpg', '9 de Paus'],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite31.jpg', '10 de Paus'],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite32.jpg', 'Valete de Paus'],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite33.jpg', 'Cavaleiro de Paus'],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite34.jpg', 'Rainha de Paus'],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite35.jpg', 'Rei de Paus'],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite36.jpg', 'Ás de Copas'],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite37.jpg', '2 de Copas'],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite38.jpg', '3 de Copas'],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite39.jpg', '4 de Copas'],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite40.jpg', '5 de Copas'],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite41.jpg', '6 de Copas'],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite42.jpg', '7 de Copas'],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite43.jpg', '8 de Copas'],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite44.jpg', '9 de Copas'],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite45.jpg', '10 de Copas'],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite46.jpg', 'Valete de Copas'],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite47.jpg', 'Cavaleiro de Copas'],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite48.jpg', 'Rainha de Copas'],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite49.jpg', 'Rei de Copas'],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite50.jpg', 'Ás de Espadas'],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite51.jpg', '2 de Espadas'],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite52.jpg', '3 de Espadas'],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite53.jpg', '4 de Espadas'],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite54.jpg', '5 de Espadas'],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite55.jpg', '6 de Espadas'],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite56.jpg', '7 de Espadas'],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite57.jpg', '8 de Espadas'],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite58.jpg', '9 de Espadas'],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite59.jpg', '10 de Espadas'],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite60.jpg', 'Valete de Espadas'],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite61.jpg', 'Cavaleiro de Espadas'],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite62.jpg', 'Rainha de Espadas'],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite63.jpg', 'Rei de Espadas'],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite64.jpg', 'Ás de Moedas'],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite65.jpg', '2 de Moedas'],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite66.jpg', '3 de Moedas'],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite67.jpg', '4 de Moedas'],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite68.jpg', '5 de Moedas'],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite69.jpg', '6 de Moedas'],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite70.jpg', '7 de Moedas'],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite71.jpg', '8 de Moedas'],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite72.jpg', '9 de Moedas'],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite73.jpg', '10 de Moedas'],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite74.jpg', 'Valete de Moedas'],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite75.jpg', 'Cavaleiro de Moedas'],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite76.jpg', 'Rainha de Moedas'],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite77.jpg', 'Rei de Moedas']
]

TodosArcanos = [
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite00.jpg', '00 - O louco'],
    ['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite01.jpg', '01 - O Mago'], 
    ['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite02.jpg', '02 - A Sacerdotisa'],
    ['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite03.jpg', '03 - A Imperatriz'],
    ['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite04.jpg', '04 - O Imperador'],
    ['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite05.jpg', '05 - O Hierofante'],
    ['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite06.jpg', '06 - Os Amantes'],
    ['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite07.jpg', '07 - O Carro'],
    ['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite08.jpg', '08 - A Força'],
    ['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite09.jpg', '09 - O Eremita'],
    ['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite10.jpg', '10 - A Roda da Fortuna'],
    ['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite11.jpg', '11 - A Justiça'],
    ['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite12.jpg', '12 - O Enforcado'],
    ['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite13.jpg', '13 - A Morte'],
    ['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite14.jpg', '14 - A Temperança'],
    ['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite15.jpg', '15 - O Diabo'],
    ['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite16.jpg', '16 - A Torre'],
    ['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite17.jpg', '17 - A Estrela'],
    ['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite18.jpg', '18 - A Lua'],
    ['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite19.jpg', '19 - O Sol'],
    ['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite20.jpg', '20 - O Julgamento'],
    ['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite21.jpg', '21 - O Mundo'],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite22.jpg', 'Ás de Paus'],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite23.jpg', '2 de Paus'],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite24.jpg', '3 de Paus'],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite25.jpg', '4 de Paus'],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite26.jpg', '5 de Paus'],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite27.jpg', '6 de Paus'],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite28.jpg', '7 de Paus'],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite29.jpg', '8 de Paus'],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite30.jpg', '9 de Paus'],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite31.jpg', '10 de Paus'],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite32.jpg', 'Valete de Paus'],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite33.jpg', 'Cavaleiro de Paus'],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite34.jpg', 'Rainha de Paus'],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite35.jpg', 'Rei de Paus'],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite36.jpg', 'Ás de Copas'],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite37.jpg', '2 de Copas'],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite38.jpg', '3 de Copas'],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite39.jpg', '4 de Copas'],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite40.jpg', '5 de Copas'],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite41.jpg', '6 de Copas'],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite42.jpg', '7 de Copas'],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite43.jpg', '8 de Copas'],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite44.jpg', '9 de Copas'],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite45.jpg', '10 de Copas'],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite46.jpg', 'Valete de Copas'],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite47.jpg', 'Cavaleiro de Copas'],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite48.jpg', 'Rainha de Copas'],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite49.jpg', 'Rei de Copas'],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite50.jpg', 'Ás de Espadas'],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite51.jpg', '2 de Espadas'],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite52.jpg', '3 de Espadas'],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite53.jpg', '4 de Espadas'],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite54.jpg', '5 de Espadas'],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite55.jpg', '6 de Espadas'],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite56.jpg', '7 de Espadas'],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite57.jpg', '8 de Espadas'],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite58.jpg', '9 de Espadas'],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite59.jpg', '10 de Espadas'],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite60.jpg', 'Valete de Espadas'],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite61.jpg', 'Cavaleiro de Espadas'],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite62.jpg', 'Rainha de Espadas'],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite63.jpg', 'Rei de Espadas'],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite64.jpg', 'Ás de Moedas'],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite65.jpg', '2 de Moedas'],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite66.jpg', '3 de Moedas'],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite67.jpg', '4 de Moedas'],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite68.jpg', '5 de Moedas'],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite69.jpg', '6 de Moedas'],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite70.jpg', '7 de Moedas'],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite71.jpg', '8 de Moedas'],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite72.jpg', '9 de Moedas'],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite73.jpg', '10 de Moedas'],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite74.jpg', 'Valete de Moedas'],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite75.jpg', 'Cavaleiro de Moedas'],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite76.jpg', 'Rainha de Moedas'],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite77.jpg', 'Rei de Moedas']
]


def start(update, context):

    update.message.reply_text('Bot ainda em testes, envia /dia para receber a carta que fala sobre o seu dia de hoje.')


def dia(update, context):

    random.shuffle(ArcanosMenores)
    random.shuffle(ArcanosMaiores)
    random.shuffle(TodosArcanos)

    #update.message.reply_text(Arcanos[0][0])
    #bot.sendPhoto(chat_id, Arcanos[0][0], Arcanos[0][1])
    chat_id = update.message.chat_id
    bot.sendPhoto(chat_id, TodosArcanos[0][0], TodosArcanos[0][1])
    #bot.sendPhoto(chat_id, ArcanosMenores[0][0], ArcanosMenores[0][1])


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









    