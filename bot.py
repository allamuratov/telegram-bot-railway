from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# /start buyrug‘iga javob beradigan funksiya
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Assalomu alaykum! Botimizga xush kelibsiz 😊")

# Botni ishga tushuruvchi asosiy funksiya
async def main():
    # Bot tokeningizni shu yerga yozing
    application = Application.builder().token("BOT_TOKENINGIZ").build()

    # /start buyrug‘i uchun handler qo‘shiladi
    application.add_handler(CommandHandler("start", start))

    # Botni ishga tushuradi
    await application.run_polling()

# Agar fayl asosiy fayl bo‘lsa, ishga tushur
if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
