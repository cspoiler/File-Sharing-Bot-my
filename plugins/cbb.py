#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>○ Creator : <a href='tg://user?id={OWNER_ID}'>This Person</a>\n○ Language : <code>Python3</code>\n○ Library : <a href='https://docs.pyrogram.org/'>Pyrogram asyncio {__version__}</a>\n○ Amazon And Filpkart loot deals : <a href='https://t.me/+KI7bmZiUzUtkM2Jl'>Click here</a>\n○ ➕↖️ I Request to Share This Message To 3 Friends ↗️➕ : <a href='https://t.me/share/url?url=Hey%20Guys%21%20If%20You%20Want%20To%20Save%20Your%20Valuable%20Money%20While%20Shopping%20On%20Flipkart%2C%20Amazon%20%26%20Paytm%20Then%20Follow%20These%20Simple%20Steps%20To%20Subscribe%20Our%20Telegram%20Channel.%20If%20You%20Have%20Already%20Subscribed%20to%20Other%20Telegram%20Channels%20And%20Not%20Getting%20Proper%20Alert%20Then%20Here%20Is%20The%20Best%20Chance%20For%20You%20To%20Grab%20Some%20Loot%20Deals.%20In%20Our%20Telegram%20Channel%2C%20We%20Provide%20All%20Amazon%20%26%20Flipkart%20Loot%20Deals%2C%20Daily%20Best%20Deals%20%26%20Price%20Error%20Offers%20At%20One%20Place.%20We%20Have%20Listed%20Some%20Price%20Error%20Offers%20%26%20Loot%20Deals.%20We%20Had%20Provided%20These%20Offers%20In%20Our%20Telegram%20Channel.%20You%20Can%20Subscribe%20Our%20Telegram%20Channel%20From%20Your%20Telegram%20App%20%26%20Web%20By%20Typing%20%27Bharat%20Offers%27%20In%20Search%20Section.%20You%20Can%20Also%20Subscribe%20Our%20Telegram%20Channel%20From%20Below%20Link.%20%0A%0Ahttps%3A//t.me/%2BKI7bmZiUzUtkM2Jl%0A%0AHey%20Guys%21%20%E0%A4%85%E0%A4%97%E0%A4%B0%20%E0%A4%86%E0%A4%AA%20Flipkart%2C%20Amazon%20%E0%A4%AA%E0%A4%B0%20%E0%A4%B6%E0%A5%89%E0%A4%AA%E0%A4%BF%E0%A4%82%E0%A4%97%20%E0%A4%95%E0%A4%B0%E0%A4%A4%E0%A5%87%20%E0%A4%B8%E0%A4%AE%E0%A4%AF%20%E0%A4%85%E0%A4%AA%E0%A4%A8%E0%A4%BE%20%E0%A4%95%E0%A5%80%E0%A4%AE%E0%A4%A4%E0%A5%80%20%E0%A4%AA%E0%A5%88%E0%A4%B8%E0%A4%BE%20%E0%A4%AC%E0%A4%9A%E0%A4%BE%E0%A4%A8%E0%A4%BE%20%E0%A4%9A%E0%A4%BE%E0%A4%B9%E0%A4%A4%E0%A5%87%20%E0%A4%B9%E0%A5%88%E0%A4%82'>Foward message</a></b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🔒 Close", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
