import api as api_key
import datetime
from telegram.ext import *


# function for the /start bot command
def start_command(update, context):
    update.message.reply_text('Welcome to Time From Now Bot!'
                              '\n\nI initally developed this telegram bot for Genshin Impact mobile players to calculate the time required to fully replenish their original resin.'
                              '\n\nHaving said that, this telegram bot can be used for any sort of "time from now" calculations.'
                              '\n\nUse the following telegram bot commands to get started:'
                              '\n/help to find out more about this bot'
                              '\n/time to display the current date and time (24-Hour Format)'
                              '\n/credits to find out more about the developer')


# function for the /help bot command
def help_command(update, context):
    update.message.reply_text('For "time from now" calculations, please enter the time in the following format:'
                              '\n\nHH:MM:SS |'
                              '\n(eg. 01:15:30) for 1 hour, 15 minutes and 30 seconds'
                              '\n(eg. 22:00:00) for 22 hours, 0 minute and 0 second'
                              '\n\nLegend:'
                              '\nHH = Hours | (eg. 01 or 24)'
                              '\nMM = Minutes | (eg. 01 or 59)'
                              '\nSS = Seconds | (eg. 01 or 59)'
                              '\n\nPlease use the telegram bots commands where applicable.')


# function for the /credits bot command
def credits_command(update, context):
    update.message.reply_text('This telegram bot was developed by BobTheBuilder.'
                              '\n(With the help of stackoverflow)')


# function for the /time bot command
def time_command(update, context):
    date_time_now = datetime.datetime.now().strftime("%d/%m/%y, %H:%M:%S %p")
    update.message.reply_text("The date and time now is: " + str(date_time_now))


# function to calculate time from now
def userinput(user_input):
    # display the current time
    time_now = datetime.datetime.now()
    time_now_str = time_now.strftime("%d/%m/%y, %H:%M:%S %p")

    # split user input into hour, minute and second
    hour = user_input.split(":", 1)[0]
    minute = user_input.split(":", 2)[1]
    second = user_input.split(":", 3)[-1]

    # display the calculated time
    time_from_now = time_now + datetime.timedelta(hours=int(hour), minutes=int(minute), seconds=int(second))
    time_from_now_str = time_from_now.strftime("%d/%m/%y, %H:%M:%S %p")

    # bot output
    bot_response = "The date and time now is: " + time_now_str + "\nResin will be refilled at: " + time_from_now_str

    # logging of user input
    print("HH:" + hour + " MM:" + minute + " SS:" + second)

    return bot_response


# function to display bot response
def bot_reply(update, context):
    user_input = update.message.text
    update.message.reply_text(userinput(user_input))


# error logging
def error(update, context):
    print(f"Update {update} caused error {context.error}")


# main process
def main():
    updater = Updater(api_key.API_KEY, use_context=True)
    dp = updater.dispatcher

    # link bot commands
    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(CommandHandler("time", time_command))
    dp.add_handler(CommandHandler("credits", credits_command))
    dp.add_handler(MessageHandler(Filters.text, bot_reply))

    # bot error
    dp.add_error_handler(error)

    # bot processes
    updater.start_polling()
    updater.idle()


# logging startup of bot
print("Time From Now Bot is running")
main()

