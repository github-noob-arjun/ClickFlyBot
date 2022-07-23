from os import environ
import datetime
import aiohttp
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

API_ID = 18988485
API_HASH = "b8b78728c7f08859bfa98f5cbb250dc8"
BOT_TOKEN = "5286545186:AAHXc48Cj366khTJvdqw500ZWdbuHPg8H48"
API_KEY = "e980180fdf60f4dff132eb393d4d3e5763480e5f"



START_BUTTONS = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton('✅ 𝗠𝗼𝗿𝗲 𝗕𝗼𝘁𝘇 ✅', url='https://t.me/PyroBotz')
        ],[
            InlineKeyboardButton('🐞 𝖱𝖾𝗉𝗈𝗋𝗍 𝖡𝗎𝗀 🐞', url='https://t.me/PYRO_BOTZ_CHAT')
        ]
    ]
)

Short = Client('clickyfly bot',
             api_id=API_ID,
             api_hash=API_HASH,
             bot_token=BOT_TOKEN,
             workers=50,
             sleep_threshold=10)


@Short.on_message(filters.command('start') & filters.private)
async def start(bot, message):
    await message.reply(
        text=f"**🙌 Hi {message.from_user.mention}!** \n\nThis is **ClickyFly URL Shorter Bot**.\nJust send me any big link and get short link.",
        reply_markup=START_BUTTONS,
        quote=True
    )

@Short.on_message(filters.regex(r'https?://[^\s]+') & filters.private)
async def link_handler(bot, message):
    link = message.matches[0].group(0)
    try:
        short_link = await get_shortlink(link)
        await message.reply(
            text=f"**link :-** `{short_link}`",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton('Open Link', url=short_link),
                        InlineKeyboardButton('Share Link', url=f"https://telegram.me/share/url?url={short_link}")
                    ],
                    [
                        InlineKeyboardButton('✅ 𝗝𝗢𝗜𝗡 𝗡𝗢𝗪 ✅', url='https://t.me/PYRO_BOTZ')
                    ]
                ]
            ),
            quote=True
        )
    except Exception as e:
        await message.reply(f'Error: {e}', quote=True)

async def get_shortlink(link):
    url = 'https://clickyfly.com/api'
    params = {'api': API_KEY, 'url': link}

    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params, raise_for_status=True) as response:
            data = await response.json()
            return data["shortenedUrl"]


