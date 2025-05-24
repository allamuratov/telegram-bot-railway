from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os
import asyncio
import nest_asyncio

nest_asyncio.apply()  # 🔧 mavjud event loop ga tuzatish

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

# Botni ishga tushirish
async def main():
    token = os.environ.get("BOT_TOKEN")
    app = ApplicationBuilder().token(token).build()

    app.add_handler(CommandHandler("start", start))
    await app.run_polling()

if __name__ == "__main__":
    asyncio.run(main())
