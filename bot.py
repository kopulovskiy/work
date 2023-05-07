from telegram.ext import Updater, CommandHolder

#obrabi4ik /start
def start(update, context):
    context.bot.send_message(chat_id=update.efective_chat.id, text="privet")

    #ekzeplyar
Updater = Updater(token='YOUR_TOKEN', use_context=True)
dispatcher = update.dispatcher 
start_handler =CommandHolder('start', start)
dispatcher.add_handler(start_handler)

#zapusk
Updater.start_polling()
