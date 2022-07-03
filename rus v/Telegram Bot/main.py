#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Simple Bot to reply to Telegram messages
# This program is dedicated to the public domain under the CC0 license.
"""
This Bot uses the Updater clast to handle the bot.

First, a few handler functions are defined. Then, those functions are pasted to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.

Usage:
Basic Echobot example, repeats messages.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler
import logging
import telegram
import parsing
# import searchmod

TOKEN = '5305305560:AAGQynMTfAWsLfCWDTlUSDDDEL1JQwqpFUk'
bot = telegram.Bot(token=TOKEN)

# Enable logging
'''
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)
'''

# Define a few command handlers. These usually take the two arguments bot and
# update. Error handlers also receive the raised TelegramError object in error.

def find(update, context):
    txt = f'Какую профессию вы выбираете?'
    context.bot.send_message(chat_id=update.effective_chat.id, text=txt)

    return 'proff'


def proff(update, context):
    context.chat_data['proff'] = f'{update.message.text}'
    context.bot.send_message(chat_id=update.effective_chat.id, text=f'Отлично, какую зарплату вы хотели бы иметь? '
                                                                    f'Напишите нижний порог оплачиваемости или '
                                                                    f'поставьте прочерк, если этот пункт не нужен.'                           
                                                                                                                    )

    return 'salary'


def salary(update, context):
    if update.message.text != '-' and not update.message.text.isdigit():
        context.bot.send_message(chat_id=update.effective_chat.id, text=f'Значение задано не верно'
                                                                        f'Пожалуйста, напишите нижний порог '
                                                                        f'оплачиваемости или поставьте прочерк, '
                                                                        f'если этот пункт не нужен.')
        return 'salary'

    context.chat_data['salary'] = f'{update.message.text}'
    context.bot.send_message(chat_id=update.effective_chat.id, text=f'Введите регион')
    return 'searching'


def searching(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=f'Ваш запрос:')
    for key in context.chat_data.keys():
        context.bot.send_message(chat_id=update.effective_chat.id, text=f'{context.chat_data[key]}')
    context.bot.send_message(chat_id=update.effective_chat.id, text=f'Начинаю поиск...')

    res = parsing.search(context.chat_data)
    context.chat_data.clear()
    context.chat_data['result'] = res

    for i in range(1, len(context.chat_data['result']) + 1):
        s = ''
        for j in range(4):
            s += str(context.chat_data['result'][i][j]) + '\n'
        context.bot.send_message(chat_id=update.effective_chat.id, text=s)
    context.chat_data.clear()

    return ConversationHandler.END


def cancel(update, _):
    return ConversationHandler.END


def start(update, context):
    # print(update.message.from_user)

    # try if None exept
    usname = update.message.from_user['username']
    txt = f'Здравствуйте {usname}, \
чтобы начать поиск подходящей работы, пожалуйста введите /find. \
Если вы хотите увидеть весь список возможного функционала, напишите /help.'
    context.bot.send_message(chat_id=update.effective_chat.id, text=txt)


'''
def find(update, context):
    txt = f'Chose one of the services'
    context.bot.send_message(chat_id=update.effective_chat.id, text=txt)
    context.chat_data['job'] = ''
    print(context.chat_data)
    check(update, context.chat_data)
    context.bot.send_message(chat_id=update.effective_chat.id, text='Ok')
'''


def help(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='Help!', reply_to_message_id=update.message.message_id)

'''
def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)
'''

'''
def error(bot, update, error):
    logger.warn('Update "%s" caused error "%s"' % (update, error))
'''


def main():
    # Create the EventHandler and past it your bot's token.
    updater = Updater(token=TOKEN)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))

    # Определяем обработчик разговоров `ConversationHandler`
    conv_handler = ConversationHandler( # здесь строится логика разговора
        # точка входа в разговор
        entry_points=[CommandHandler('find', find)],
        # этапы разговора, каждый со своим списком обработчиков сообщений
        states={'proff': [MessageHandler(Filters.text, proff)], 'salary': [MessageHandler(Filters.text, salary)],
                'searching': [MessageHandler(Filters.text, searching)]
               },
        # точка выхода из разговора
        fallbacks=[CommandHandler('cancel', cancel)],
    )

    dp.add_handler(conv_handler)


    # dp.add_handler(CommandHandler("find", find))

    # on noncommand i.e message - echo the message on Telegram
    # dp.add_handler(MessageHandler(Filters.text, echo))

    # log all errors
    # dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until the you presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()