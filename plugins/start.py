import os
import asyncio
from pyrogram import Client, filters, __version__
from pyrogram.enums import ParseMode
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from pyrogram.errors import FloodWait, UserIsBlocked, InputUserDeactivated

from bot import Bot
from config import ADMINS, FORCE_MSG, START_MSG, CUSTOM_CAPTION, DISABLE_CHANNEL_BUTTON, PROTECT_CONTENT
from helper_func import subscribed, encode, decode, get_messages
from database.database import add_user, del_user, full_userbase, present_user

async def delete_after_delay(message: Message, delay):
    await asyncio.sleep(delay)
    await message.delete()

@Bot.on_message(filters.command('start') & filters.private & subscribed)
async def start_command(client: Client, message: Message):
    id = message.from_user.id
    if not await present_user(id):
        try:
            await add_user(id)
        except:
            pass
    text = message.text
    if len(text) > 7:
        try:
            base64_string = text.split(" ", 1)[1]
        except:
            return
        string = await decode(base64_string)
        argument = string.split("-")
        if len(argument) == 3:
            try:
                start = int(int(argument[1]) / abs(client.db_channel.id))
                end = int(int(argument[2]) / abs(client.db_channel.id))
            except:
                return
            if start <= end:
                ids = range(start, end + 1)
            else:
                ids = []
                i = start
                while True:
                    ids.append(i)
                    i -= 1
                    if i < end:
                        break
        elif len(argument) == 2:
            try:
                ids = [int(int(argument[1]) / abs(client.db_channel.id))]
            except:
                return
        temp_msg = await message.reply("Please wait...")

        # Warning Message in English
        warning_msg_en = await message.reply_text("⚠️ <b>Warning:</b> This message will be automatically deleted in 1 minute ⏳", parse_mode=ParseMode.HTML)
        asyncio.create_task(delete_after_delay(warning_msg_en, 60))  # Schedule the deletion of the warning message after 1 minute

        # Warning Message in Hindi
        warning_msg_hi = await message.reply_text("⚠️ <b>चेतावनी:</b> यह संदेश स्वचालित रूप से 1 मिनट में हटा दिया जाएगा ⏳", parse_mode=ParseMode.HTML)
        asyncio.create_task(delete_after_delay(warning_msg_hi, 60))  # Schedule the deletion of the warning message after 1 minute

        try:
            messages = await get_messages(client, ids)
        except:
            await message.reply_text("Something went wrong..!")
            return
        await temp_msg.delete()

        for msg in messages:
            if bool(CUSTOM_CAPTION) & bool(msg.document):
                caption = CUSTOM_CAPTION.format(previouscaption="" if not msg.caption else msg.caption.html,
                                                filename=msg.document.file_name)
            else:
                caption = "" if not msg.caption else msg.caption.html

            if DISABLE_CHANNEL_BUTTON:
                reply_markup = msg.reply_markup
            else:
                reply_markup = None

            try:
                new_msg = await msg.copy(chat_id=message.from_user.id, caption=caption, parse_mode=ParseMode.HTML,
                                         reply_markup=reply_markup, protect_content=PROTECT_CONTENT)

                # Schedule the deletion of the new message after 1 minute
                asyncio.create_task(delete_after_delay(new_msg, 60))  # 60 seconds = 1 minute

                await asyncio.sleep(0.5)
            except FloodWait as e:
                await asyncio.sleep(e.x)
                new_msg = await msg.copy(chat_id=message.from_user.id, caption=caption, parse_mode=ParseMode.HTML,
                                         reply_markup=reply_markup, protect_content=PROTECT_CONTENT)

                # Schedule the deletion of the new message after 1 minute
                asyncio.create_task(delete_after_delay(new_msg, 60))  # 60 seconds = 1 minute
            except:
                pass

        return
    else:
        reply_markup = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton('⚡🆓 Amazon Loot Deals 🆓⚡',
                                         url=f'https://t.me/+KI7bmZiUzUtkM2Jl')
                ],
                [
                    InlineKeyboardButton('⚡️↖️ I Request to Share This Message To Your 3 Friends ↗️⚡️',
                                         url=f'https://t.me/share/url?url=Hey%20Guys%21%20If%20You%20Want%20To%20Save%20Your%20Valuable%20Money%20While%20Shopping%20On%20Flipkart%2C%20Amazon%20%26%20Paytm%20Then%20Follow%20These%20Simple%20Steps%20To%20Subscribe%20Our%20Telegram%20Channel.%20If%20You%20Have%20Already%20Subscribed%20to%20Other%20Telegram%20Channels%20And%20Not%20Getting%20Proper%20Alert%20Then%20Here%20Is%20The%20Best%20Chance%20For%20You%20To%20Grab%20Some%20Loot%20Deals.%20In%20Our%20Telegram%20Channel%2C%20We%20Provide%20All%20Amazon%20%26%20Flipkart%20Loot%20Deals%2C%20Daily%20Best%20Deals%20%26%20Price%20Error%20Offers%20At%20One%20Place.%20We%20Have%20Listed%20Some%20Price%20Error%20Offers%20%26%20Loot%20Deals.%20We%20Had%20Provided%20These%20Offers%20In%20Our%20Telegram%20Channel.%20You%20Can%20Subscribe%20Our%20Telegram%20Channel%20From%20Your%20Telegram%20App%20%26%20Web%20By%20Typing%20%27Bharat%20Offers%27%20In%20Search%20Section.%20You%20Can%20Also%20Subscribe%20Our%20Telegram%20Channel%20From%20Below%20Link.%20%0A%0Ahttps%3A//t.me/%2BKI7bmZiUzUtkM2Jl%0A%0AHey%20Guys%21%20%E0%A4%85%E0%A4%97%E0%A4%B0%20%E0%A4%86%E0%A4%AA%20Flipkart%2C%20Amazon%20%E0%A4%AA%E0%A4%B0%20%E0%A4%B6%E0%A5%89%E0%A4%AA%E0%A4%BF%E0%A4%82%E0%A4%97%20%E0%A4%95%E0%A4%B0%E0%A4%A4%E0%A5%87%20%E0%A4%B8%E0%A4%AE%E0%A4%AF%20%E0%A4%85%E0%A4%AA%E0%A4%A8%E0%A4%BE%20%E0%A4%95%E0%A5%80%E0%A4%AE%E0%A4%A4%E0%A5%80%20%E0%A4%AA%E0%A5%88%E0%A4%B8%E0%A4%BE%20%E0%A4%AC%E0%A4%9A%E0%A4%BE%E0%A4%A8%E0%A4%BE%20%E0%A4%9A%E0%A4%BE%E0%A4%B9%E0%A4%A4%E0%A5%87%20%E0%A4%B9%E0%A5%88%E0%A4%82')
                ],
                [
                    InlineKeyboardButton("😊 About Me", callback_data="about"),
                    InlineKeyboardButton("🛑 Support", url=f'https://t.me/Bharat_Offers_Supportbot')
                ],
                [
                    InlineKeyboardButton("🔒 Close", callback_data="close")
                ]
            ]
        )

        await message.reply_text(
            text=START_MSG.format(
                first=message.from_user.first_name,
                last=message.from_user.last_name,
                username=None if not message.from_user.username else '@' + message.from_user.username,
                mention=message.from_user.mention,
                id=message.from_user.id
            ),
            reply_markup=reply_markup,
            disable_web_page_preview=True,
            quote=True
        )
        return


#=====================================================================================##

WAIT_MSG = """"<b>Processing ...</b>"""

REPLY_ERROR = """<code>Use this command as a replay to any telegram message with out any spaces.</code>"""

#=====================================================================================##

async def update_timer(timer_msg: Message, seconds: int):
    while seconds > 0:
        await asyncio.sleep(1)
        seconds -= 1
        await timer_msg.edit_text(f"⏳ <b>Time Left:</b> {seconds} seconds", parse_mode=ParseMode.HTML)

@Bot.on_message(filters.command('start') & filters.private)
async def not_joined(client: Client, message: Message):
    buttons = [
        [InlineKeyboardButton('⚡ 𝐑𝐞𝐪𝐮𝐞𝐬𝐭 𝐭𝐨 𝐣𝐨𝐢𝐧 1 ⚡', url="https://t.me/+raySqD7AFY43MGNl")],
        [
            InlineKeyboardButton(
                "⚡ 𝐑𝐞𝐪𝐮𝐞𝐬𝐭 𝐭𝐨 𝐣𝐨𝐢𝐧 2 ⚡",
                url="https://t.me/+PTBUOr8UPrk4NmI1")
        ],
        [
            InlineKeyboardButton(
                "⚡ 𝐑𝐞𝐪𝐮𝐞𝐬𝐭 𝐭𝐨 𝐣𝐨𝐢𝐧 3 ⚡",
                url=client.invitelink)
        ]
    ]
    try:
        buttons.append(
            [
                InlineKeyboardButton(
                    text='𝐓𝐫𝐲 𝐀𝐠𝐚𝐢𝐧',
                    url=f"https://t.me/{client.username}?start={message.command[1]}"
                )
            ]
        )
    except IndexError:
        pass

    await message.reply(
        text=FORCE_MSG.format(
            first=message.from_user.first_name,
            last=message.from_user.last_name,
            username=None if not message.from_user.username else '@' + message.from_user.username,
            mention=message.from_user.mention,
            id=message.from_user.id
        ),
        reply_markup=InlineKeyboardMarkup(buttons),
        quote=True,
        disable_web_page_preview=True
    )

@Bot.on_message(filters.command('users') & filters.private & filters.user(ADMINS))
async def get_users(client: Bot, message: Message):
    msg = await client.send_message(chat_id=message.chat.id, text=WAIT_MSG)
    users = await full_userbase()
    await msg.edit(f"{len(users)} users are using this bot")

@Bot.on_message(filters.private & filters.command('broadcast') & filters.user(ADMINS))
async def send_text(client: Bot, message: Message):
    if message.reply_to_message:
        query = await full_userbase()
        broadcast_msg = message.reply_to_message
        total = 0
        successful = 0
        blocked = 0
        deleted = 0
        unsuccessful = 0

        pls_wait = await message.reply("<i>Broadcasting Message.. This will Take Some Time</i>")
        for chat_id in query:
            try:
                await broadcast_msg.copy(chat_id)
                successful += 1
            except FloodWait as e:
                await asyncio.sleep(e.x)
                await broadcast_msg.copy(chat_id)
                successful += 1
            except UserIsBlocked:
                await del_user(chat_id)
                blocked += 1
            except InputUserDeactivated:
                await del_user(chat_id)
                deleted += 1
            except:
                unsuccessful += 1
                pass
            total += 1

        status = f"""<b><u>Broadcast Completed</u>

Total Users: <code>{total}</code>
Successful: <code>{successful}</code>
Blocked Users: <code>{blocked}</code>
Deleted Accounts: <code>{deleted}</code>
Unsuccessful: <code>{unsuccessful}</code></b>"""

        return await pls_wait.edit(status)

    else:
        msg = await message.reply(REPLY_ERROR)
        await asyncio.sleep(8)
        await msg.delete()

if __name__ == "__main__":
    Bot.run()
