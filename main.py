import logging
from helper_funtions import append_json

from telegram import Bot, Update, helpers
from safe import BOT_TOKEN
from telegram.ext import CommandHandler, MessageHandler, filters, ContextTypes, Application

# The bot token

TOKEN = BOT_TOKEN

# define a dictionary that keeps track of user states

user_states = {}

# basic logging config. I'll setup some more when I understand how the logging module fully works

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.WARNING
)
bot = Bot(TOKEN)

# Commands

# start command that does something will setup something later.

async def start(update:Update, context: ContextTypes) -> None:
    await context.bot.send_message(chat_id= update.effective_chat.id ,text='The bot is now online!')

# Command to store user files

async def store(update: Update, context: ContextTypes.DEFAULT_TYPE):

    # Get the user chat id

    chat_id = update.message.chat_id

    # set the user state for the effective chat to true
    '''
    what this does is make such the particular user who used the command is
    given the value of true. When we handle the response we're going to check
    whether the state for that particular use is set to True and if it is we will
    store the files. If it is not we're going to suggest other methods to proceed.
    '''
    user_states[chat_id] = True

    await context.bot.send_message(chat_id=update.message.chat.id, text="Please send the files you want to store")



async def handle_media_to_store(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.message.chat_id
    bot_username = context.bot.username

    # Check whether the user state is True
    if user_states[chat_id]:

        # Get the file from the Update

        document = update.message.document

        # test if we got the file from the update
        if document:

            # Get the necessary info to store to the json file

            # This is the same as update.message.chat.id
            chat_id = update.message.chat_id 
            message_id = update.message.message_id
            file_id = document.file_id
            cows_are_cool = 'cows-are-cool'
            link = helpers.create_deep_linked_url(context.bot.username, cows_are_cool, group=True)

            data = {
                str(chat_id): {
                    "message_id": message_id,
                    "file_id": file_id,
                    "file_link": link
                }
            }

            append_json(data)

            reply_text = f'The file has been saved. Use this link to get the file {link}'

            print('data saved to database')

            # Change the user state to False to ensure the end of the interaction.

            return await context.bot.send_message(chat_id=chat_id, text=reply_text)
        



def main():

    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler('start', start))
    app.add_handler(CommandHandler('store', store, filters=filters.PHOTO | filters.TEXT))
    app.add_handler(MessageHandler(filters.ALL, handle_media_to_store))

    app.run_polling()


if __name__ == "__main__":
    main()