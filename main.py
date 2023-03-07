import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

bot_token: str = os.environ.get("BOT_TOKEN")

chat_id = "313782761"


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')


app = ApplicationBuilder().token("6172692800:AAH1wVMOcohvcaeOuZDL2GybHFlkn8g198A").build()

app.add_handler(CommandHandler("hello", hello))

app.run_polling()
