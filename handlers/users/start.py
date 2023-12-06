import sqlite3

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from keyboards.default.startbut import default_button

from data.config import ADMINS
from loader import dp, db, bot


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    name = message.from_user.full_name
    try:
        db.add_user(id=message.from_user.id,
                    name=name)
        await message.answer(f"🇷🇺 Добро пожаловать! {name}\n 🇺🇿 Xush kelibsiz! {name}", reply_markup= default_button)
        # Adminga xabar beramiz
        count = db.count_users()[0]
        msg = f"{message.from_user.full_name} добавлен в базу.\nВ базе {count} участников."
        await bot.send_message(chat_id=ADMINS[0], text=msg)

    except sqlite3.IntegrityError as err:
        await bot.send_message(chat_id=ADMINS[0], text=f"{name} уже добавлен в базу.")
        await message.answer(f" 🇷🇺 Добро пожаловать! {name} \n 🇺🇿 Xush kelibsiz! {name}",reply_markup= default_button)


#<----------BUTTONS--------------->

@dp.message_handler(text='♾️Kanal')
async def freeagentts(message: types.Message):
    await message.answer('🇷🇺 Наш канал для трейдеров \n 🇺🇿 Bizning treyderlar kanali \n https://t.me/Khiva_Traders ', reply_markup = default_button)

@dp.message_handler(text='🔉Goloslar')
async def freeagentts(message: types.Message):
    await message.answer(' ', reply_markup = default_button)