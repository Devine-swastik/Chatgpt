import logging
from pyrogram import Client, filters, idle
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
import openai
import os
import time
from datetime import datetime

# Logging configuration
FORMAT = "[%(asctime)s] [%(levelname)s] [%(name)s] - %(message)s"
logging.basicConfig(
    level=logging.WARNING,
    format=FORMAT,
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger(__name__)

# Get environment variables
API_ID = int(os.getenv('API_ID', 29644708))
API_HASH = os.getenv('API_HASH', '0db39046c635489ccb05d9a0ca395c9f')
BOT_TOKEN = os.getenv('BOT_TOKEN', '7866262568:AAG-DzguR8kK6B7dzFQW53RFxoUUmeLzQsg')
BOT_NAME = os.getenv('BOT_NAME', 'Chat Gpt')
BOT_USERNAME = os.getenv('BOT_USERNAME', 'Devine_chatgpt_bot')
OWNER_ID = int(os.getenv('OWNER_ID', '6338745050'))
OWNER_USERNAME = os.getenv('OWNER_USERNAME', 'devine4x')
UPDATE_CHANNEL = os.getenv('UPDATE_CHANNEL', 'Devine_Network')
SUPPORT_GROUP = os.getenv('SUPPORT_GROUP', "Devine_Network")

# OpenAI Configuration
OPENAI_KEY = os.getenv('OPENAI_KEY', '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')

# MongoDB Configuration
MONGODB_URL = os.getenv('MONGODB_URL', 'mongodb+srv://godofgenjutsu9229:K2HFlJA7EbSZjC6Z@cluster0.l6zam.mongodb.net/?retryWrites=true&w=majority')

# Check if all re

DEVINE = Client(
    "chat-gpt",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

START = f"""
<b>ɢʀᴇᴇᴛɪɴɢs, ɪ ᴀᴍ {BOT_NAME}</b>

<b>──────────────────</b>
<b>ᴀɴ ᴀᴅᴠᴀɴᴄᴇᴅ ᴀʟɢᴏʀɪᴛʜᴍs,
ɪ ᴄᴀɴ ʀᴇsᴏʟᴠᴇ ʏᴏᴜʀ ǫᴜᴇʀɪᴇs ᴡɪᴛʜ
ʟɪɢʜᴛɴɪɴɢ sᴘᴇᴇᴅ ᴀɴᴅ ᴀᴄᴄᴜʀᴀᴄʏ.</b>"""

MAIN_BUTTONS = [
    [
        InlineKeyboardButton(text="ᴀᴅᴅ ᴍᴇ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ", url=f"https://t.me/{BOT_USERNAME}?startgroup=true"),
    ],
    [
        InlineKeyboardButton(text="ᴅᴇᴠᴇʟᴏᴘᴇʀ", url=f"https://t.me/{OWNER_USERNAME}"),
        InlineKeyboardButton(text="sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ", url="\x68\x74\x74\x70\x73\x3a\x2f\x2f\x67\x69\x74\x68\x75\x62\x2e\x63\x6f\x6d\x2f\x64\x65\x76\x69\x6e\x65\x70\x61\x72\x61\x64\x6f\x78\x2f\x44\x65\x76\x69\x6e\x65\x2d\x43\x68\x61\x74\x2d\x47\x70\x74"),
    ],
    [
        InlineKeyboardButton(text="ʜᴇʟᴘ & ᴄᴏᴍᴍᴀɴᴅs", callback_data="HELP"),
    ],
]

HELP_READ = "ᴜsᴀɢᴇ /chatgpt <prompt>\n\n ᴇxᴀᴍᴘʟᴇ: `/chatgpt write a simple flask app in python.`\n\n**➻ ᴜsᴀɢᴇ** : /generate <prompt> \nᴇxᴀᴍᴘʟᴇ: `/generate a message to comfort a friend `"

HELP_BACK = [
    [
        InlineKeyboardButton(text="ʙᴀᴄᴋ ", callback_data="HELP_BACK"),
    ],
]

@DEVINE.on_message(filters.command(["start", f"start@{BOT_USERNAME}"]))
async def start(client, message: Message):
    try:
        await message.reply_photo(
            photo=START_IMG,
            caption=START,
            reply_markup=InlineKeyboardMarkup(MAIN_BUTTONS),
        )
    except Exception as e:
        logger.error(f"Error in start command: {e}")
        await message.reply_text(f"Error: {e}")

@DEVINE.on_callback_query()
async def cb_handler(client, query):
    if query.data == "HELP":
        await query.message.edit_text(
            text=HELP_READ,
            reply_markup=InlineKeyboardMarkup(HELP_BACK),
        )
    elif query.data == "HELP_BACK":
        await query.message.edit_text(
            text=START,
            reply_markup=InlineKeyboardMarkup(MAIN_BUTTONS),
        )

@DEVINE.on_message(filters.command(["help", f"help@{BOT_USERNAME}"], prefixes=["", "+", ".", "/", "-", "?", "$"]))
async def help(client, message: Message):
    await message.reply_photo(
        START_IMG,
        caption=HELP_READ,
        reply_markup=InlineKeyboardMarkup(HELP_BACK),
    )

@DEVINE.on_message(filters.command(["ping", "alive"], prefixes=["+", "/", "-", "?", "$", "&", "."]))
async def ping(client, message: Message):
    # Start loading animation
    loading_msg = await message.reply_text("🔥")
    await asyncio.sleep(0.4)
    await loading_msg.edit_text("⚡")
    await asyncio.sleep(0.5)
    
    # Calculate ping response time
    start_time = datetime.now()
    await message.reply_text("Ꮮᴏᴀᴅɪɴɢ...")
    await asyncio.sleep(0.7)
    end_time = datetime.now()
    ms = (end_time - start_time).microseconds / 1000
    
    # Send ping response
    await message.reply_photo(
        photo=START_IMG,
        caption=f"✨ {BOT_NAME} ɪs ᴀʟɪᴠᴇ.\n\n"
                f"‣ ᴍᴀᴅᴇ ʙʏ [ᴅᴇᴠɪɴᴇ ɴᴇᴛᴡᴏʀᴋ](https://t.me/Devine_Network)\n"
                f"‣ ᴅᴇᴠʟᴏᴘᴇʀ : [Ꭰᴇᴠɪɴᴇ Ꭰᴀʀᴋ 々](https://t.me/Devine_dark)\n"
                f"‣ ᴘɪɴɢ : {ms} ᴍs\n"
                f"‣ ᴘʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ : 𝟸.𝟺.𝟸\n"
                f"‣ ᴘʏʀᴏɢʀᴀᴍ ᴠᴇʀsɪᴏɴ : 𝟸.𝟶.𝟷𝟶𝟼",
    )
    openai.api_key = OPENAI_KEY  # Ensure this line is at the top level, not inside any function or class

@DEVINE.on_message(filters.command(["chatgpt", "ai", "ask"], prefixes=["+", ".", "/", "-", "?", "$", "#", "&"]))
async def chat(client, message: Message):
    try:
        if len(message.command) < 2:
            await message.reply_text("Example:\n\n`/chatgpt Where is the Taj Mahal?`")
        else:
            prompt = message.text.split(' ', 1)[1]
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.2,
            )
            reply_text = response['choices'][0]['message']['content']
            await message.reply_text(reply_text)
    except Exception as e:
        logger.error(f"Error in chat command: {e}")
        await message.reply_text(f"Error: {e}")

if __name__ == "__main__":
    try:
        logger.info("Bot is starting...")
        DEVINE.run()
        idle()
    except Exception as e:
        logger.error(f"Bot encountered an error: {e}")
    finally:
        logger.info("Bot has stopped.")
