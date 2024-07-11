import nest_asyncio
import asyncio
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ApplicationBuilder, CommandHandler

# Ваш токен Telegram Bot API
TOKEN = '6948544716:AAHMNgin0baIxKdSDGe3CfUV_9yppf8rAZQ'

# Применить nest_asyncio
nest_asyncio.apply()

async def start(update: Update, context) -> None:
    keyboard = [[InlineKeyboardButton("Open Game", url="https://braindom-ullu.github.io/CatSoupGame/")]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text('Click the button below to play the game:', reply_markup=reply_markup)

async def main():
    print("Starting the bot...")
    application = ApplicationBuilder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))

    print("Bot is polling...")
    await application.run_polling()

if __name__ == '__main__':
    asyncio.run(main())

