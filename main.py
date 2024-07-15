from telegram import Bot, Update
from safe import BOT_TOKEN
from telegram.ext import CommandHandler, MessageHandler, filters, ContextTypes, Application

TOKEN = 

bot = Bot(TOKEN)


#commands
async def start(update:Update, context: ContextTypes) -> None:
    await context.bot.send_message(chat_id= update.effective_chat.id ,text='The bot is now online!')

async def store(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await bot.send_message(chat_id=update.message.chat.id, text="Please send the files you want to store")
    await collect_files(update, context)
    # await update.message
    # print(update.message)
   


# message handles

async def collect_files(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message:
        document = update.message.document
        unique_id = document.file_unique_id
        print(document.file_unique_id)
        chat_id = update.message.chat_id
        # file_id = update.message.document.file_unique_id
        # print(update.message)

    else:
        print('no update was recieved')

def store_files():
    pass




# defining entry points

def main():

    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler('start', start))
    app.add_handler(CommandHandler('store', store))
    app.add_handler(MessageHandler(filters.ALL, collect_files))

    app.run_polling()


if __name__ == "__main__":
    main()