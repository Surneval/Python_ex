from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import datetime
import asyncio
from spy import *

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    log_command(update, context)
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    log_command(update, context)
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')

async def time(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    log_command(update, context)
    await update.message.reply_text(f'Time {datetime.datetime.now().time()}')

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    log_command(update, context)
    await update.message.reply_text(f'/hello\n/time\n/help')

async def sum(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log_command(update, context)
    msg = update.message.text
    print({msg})
    items = msg.split() # /sum 123 123
    x = int(items[1])
    y = int(items[2])

    await update.message.reply_text(f'{x} + {y} = {x + y}')

app = ApplicationBuilder().token("5791740111:AAHeiS9eQdMPhxcJtPgO9fQKBucMkV-imUs").build()

app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("time", time))
app.add_handler(CommandHandler("help", help))
app.add_handler(CommandHandler("sum", sum))
print("start server")
app.run_polling()