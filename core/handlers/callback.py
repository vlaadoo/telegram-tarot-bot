from aiogram import Bot, Dispatcher
from aiogram.types import CallbackQuery, FSInputFile
from aiogram import exceptions
import asyncio
import random
from core.keyboards.inline import stop_card_of_day
from infobase import card_desc, cards


from aiogram.fsm.context import FSMContext
from core.handlers.basic import layout_change

is_running = {}




async def select_card_of_day(call: CallbackQuery, bot: Bot):
    chat_id = call.message.chat.id
    if is_running.get(chat_id):
        is_running[chat_id] = False
        return
    is_running[chat_id] = True
    message = await bot.send_message(chat_id, "Выбираем карту")
    message = await bot.send_message(chat_id, random.choice(cards))
    await call.answer()
    while is_running.get(chat_id):
        for card in cards:
            if not is_running.get(chat_id):
                break
            await asyncio.sleep(0.1)  # задержка в 1 секунду
            try:
                await bot.edit_message_text(card, chat_id, message.message_id, reply_markup=stop_card_of_day)
            except exceptions.TelegramBadRequest:
                continue
    is_running[chat_id] = False
        
async def stop_card_of_day_handler(call: CallbackQuery, bot: Bot):
    chat_id = call.message.chat.id
    is_running[chat_id] = False
    temp_daycard = random.randint(0, 21)
    message_caption = "Ваш аркан дня: " + str(temp_daycard) + "\nОписание вашего аркана дня: " + card_desc[temp_daycard]
    photo_path = './cards/card' + str(temp_daycard) + '.jpeg'
    await bot.delete_message(chat_id, call.message.message_id)  # удаление старого сообщения
    await bot.send_photo(chat_id, FSInputFile(photo_path), caption=message_caption)    
    await call.answer()

async def change_layout(call: CallbackQuery, state: FSMContext, bot: Bot):
    await bot.send_message(call.from_user.id, 'Введите название расклада!')
    await layout_change(call, state)


async def layout_1_call(call: CallbackQuery, state: FSMContext, bot: Bot):
    with open('./1.txt', 'r', encoding='utf-8') as f:
        await bot.send_message(call.from_user.id, f.read())
    await call.answer()

async def layout_2_call(call: CallbackQuery, state: FSMContext, bot: Bot):
    with open('./2.txt', 'r', encoding='utf-8') as f:
        await bot.send_message(call.from_user.id, f.read())
    await call.answer()

async def layout_3_call(call: CallbackQuery, state: FSMContext, bot: Bot):
    with open('./3.txt', 'r', encoding='utf-8') as f:
        await bot.send_message(call.from_user.id, f.read())
    await call.answer()