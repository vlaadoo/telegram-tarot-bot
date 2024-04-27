import json
from aiogram import Bot, Dispatcher
from aiogram.types import CallbackQuery, FSInputFile
from aiogram import exceptions
import asyncio
import random
from core.horoscope.get_text_horoscope import get_text_horoscope
from core.keyboards.inline import get_zodiac_keyboard, show_cards_arcans_kb, \
    edit_cards_arcans_kb, edit_big_arcans_kb, edit_pentacli_kb, edit_zhezly_kb, edit_mechi_kb, edit_chashi_kb, \
    show_big_arcans_kb, show_pentacli_kb, show_zhezly_kb, show_mechi_kb, show_chashi_kb
from infobase import card_desc, cards
import config
from core.database.database import get_card_name, get_random_row, get_card_desc, get_layout_from_db

from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from core.handlers.basic import layout_change

import re


is_running = {}

class UpdateBigCard(StatesGroup):
    card_id = State()
    description = State()

async def select_card_of_day(call: CallbackQuery, bot: Bot):
    chat_id = call.message.chat.id
    daycard = get_random_row()
    message_caption = f"Ваша карта дня: {daycard[2]}\nОписание карты:\n{daycard[3]}"
    photo_path = './cards/' + daycard[1]
    await bot.delete_message(chat_id, call.message.message_id)  # удаление старого сообщения
    await bot.send_photo(chat_id, FSInputFile(photo_path), caption=message_caption)    
    await call.answer()
    
async def select_card_of_day_2(call: CallbackQuery, bot: Bot):
    chat_id = call.message.chat.id
    daycard = get_random_row()
    message_caption = f"Карта дня: {daycard[2]}\nОписание карты:\n{daycard[3]}"
    photo_path = './cards/' + daycard[1]
    print(message_caption)
    # await bot.delete_message(chat_id, call.message.message_id)  # удаление старого сообщения
    # await bot.send_photo(chat_id, FSInputFile(photo_path), caption=message_caption)    
    await call.answer(message_caption[:200], show_alert=True)

async def change_layout(call: CallbackQuery, state: FSMContext, bot: Bot):
    await bot.send_message(call.from_user.id, 'Введите название расклада!')
    await layout_change(call, state)
    
async def layout_call(call: CallbackQuery, state: FSMContext, bot: Bot):
    number = re.findall(r'\d+', call.data)
    print(number)
    values = json.loads(get_layout_from_db()[2])
    await call.answer(values[int(number[0]) - 1], show_alert=True)

async def get_horoscope_call(call: CallbackQuery):
    zodiac = call.data
    sentences = re.split('(?<=[.])\\s', await get_text_horoscope(zodiac=zodiac))
    message_text = random.choice(sentences)
    await call.answer(text=message_text, show_alert=True)
    

# --------Изменение описания карт--------
async def edit_cards(call: CallbackQuery):
    await call.message.edit_text('Изменение карт. Выбор арканы', reply_markup=edit_cards_arcans_kb())
    await call.answer()
    
async def edit_big_arcans(call: CallbackQuery):
    await call.message.edit_text('Старшие арканы. Выбор карты', reply_markup=edit_big_arcans_kb())
    await call.answer()
    
async def edit_pentacli(call: CallbackQuery):
    await call.message.edit_text('Пентакли. Выбор карты', reply_markup=edit_pentacli_kb())
    await call.answer()
    
async def edit_zhezly(call: CallbackQuery):
    await call.message.edit_text('Жезлы. Выбор карты', reply_markup=edit_zhezly_kb())
    await call.answer()
    
async def edit_mechi(call: CallbackQuery):
    await call.message.edit_text('Мечи. Выбор карты', reply_markup=edit_mechi_kb())
    await call.answer()

async def edit_chashi(call: CallbackQuery, bot: Bot):
    await call.message.edit_text('Чаши. Выбор карты', reply_markup=edit_chashi_kb())
    await call.answer()
    
async def edit_card_id(call: CallbackQuery, state: FSMContext, bot: Bot):
    await call.answer()
    await state.update_data(card_id = call.data)
    await state.set_state(UpdateBigCard.description)
    title = get_card_name(call.data)
    await bot.send_message(call.from_user.id, 'Введите описание для карты: ' + title)
    
# ----- Просмотр карт -----
async def show_cards(call: CallbackQuery):
    await call.message.edit_text('Просмотр карт. Выбор арканы для просмотра', reply_markup=show_cards_arcans_kb())
    await call.answer()
    
async def show_big_arcans(call: CallbackQuery):
    await call.message.edit_text('Старшие арканы. Выбор карты для просмотра', reply_markup=show_big_arcans_kb())
    await call.answer()
    
async def show_pentacli(call: CallbackQuery):
    await call.message.edit_text('Пентакли. Выбор карты для просмотра', reply_markup=show_pentacli_kb())
    await call.answer()
    
async def show_zhezly(call: CallbackQuery):
    await call.message.edit_text('Жезлы. Выбор карты для просмотра', reply_markup=show_zhezly_kb())
    await call.answer()
    
async def show_mechi(call: CallbackQuery):
    await call.message.edit_text('Мечи. Выбор карты для просмотра', reply_markup=show_mechi_kb())
    await call.answer()

async def show_chashi(call: CallbackQuery, bot: Bot):
    await call.message.edit_text('Чаши. Выбор карты для просмотра', reply_markup=show_chashi_kb())
    await call.answer()
    
async def show_card_details(call: CallbackQuery):
    card_id = call.data
    card = get_card_desc(card_id.split('_')[0])
    await call.message.edit_text("Карта:\n" + card[0] + '\nОписание:\n' + card[1])
    await call.answer()