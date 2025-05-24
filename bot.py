from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os
import asyncio

# /start komandasi uchun funksiya
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    group_link = "https://t.me/nokis_tashken_almati"
    keyboard = [[InlineKeyboardButton("👥 Guruhga qo‘shilish", url=group_link)]]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "Assalomu alaykum!\n\nQuyidagi tugma orqali guruhimizga qo‘shiling: \n"
        "https://t.me/nokis_tashken_almati\n"
        "https://t.me/tashkent_nokis1",
        reply_markup=reply_markup
    )

# Railway uchun oddiy ishga tushirish (asyncio.run() ishlatmasdan)
async def main():
    token = os.environ.get("BOT_TOKEN")  # Railway'da ENV o'rnatiladi
    app = ApplicationBuilder().token(token).build()
    app.add_handler(CommandHandler("start", start))

    await app.run_polling()  # Bu o'zi event loopni boshqaradi

# Railway bilan mos - faqat asyncio event loop ishlatiladi
if __name__ == "__main__":
    asyncio.run(main())
