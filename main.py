import logging
from helper_funtions import store_files

from telegram import Bot, Update
from safe import BOT_TOKEN
from telegram.ext import CommandHandler, MessageHandler, filters, ContextTypes, Application

TOKEN = BOT_TOKEN

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
bot = Bot(TOKEN)

#commands
async def start(update:Update, context: ContextTypes) -> None:
    await context.bot.send_message(chat_id= update.effective_chat.id ,text='The bot is now online!')

async def store(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.message.chat.id, text="Please send the files you want to store")
    photo = update.message.photo

    if photo:
        incoming_file_id = photo.file_id
        chat_id = update.message.chat_id
        message_id = update.message.message_id
        store_files(chat_id, message_id, incoming_file_id)

    print('data saved to database')
        
        
    # await update.message
    # print(update.message)
   


# message handles

# async def collect_files(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     if update.message:
#         document = update.message.document
#         file_id = document.file_id
#         await context.bot.send_message(chat_id=update.message.chat_id, text=file_id)
#         chat_id = update.message.chat_id
#         # file_id = update.message.document.file_unique_id
#         # print(update.message)

    # else:
    #     print('no update was recieved')





# defining entry points

def main():

    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler('start', start))
    app.add_handler(CommandHandler('store', store))
    # app.add_handler(MessageHandler(filters.PHOTO and filters.VIDEO and filters.ATTACHMENT, collect_files))

    app.run_polling()


if __name__ == "__main__":
    main()