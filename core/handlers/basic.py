from aiogram import Bot
from aiogram.types import Message, FSInputFile
from aiogram.filters import CommandObject
from core.keyboards.inline import edit_cards_arcans_kb, start_card_of_day, admin_panel_inline, layout_inline, get_zodiac_keyboard
from core.keyboards.reply import reply_keyboard_user
import config
from core.database.database import save_new_layout, update_card_desc, get_layout_from_db

from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from datetime import datetime

class Layout(StatesGroup):
    title = State()
    image = State()
    layout_1_context = State()
    layout_2_context = State()
    layout_3_context = State()
    layout_context = State()

async def cmd_start(message: Message, bot=Bot):
    await message.answer(f'Привет, {message.from_user.first_name}, добро пожаловать!', reply_markup=reply_keyboard_user)


async def get_day_card(message: Message, command: CommandObject, bot=Bot):
    if message.from_user.id in config.ADMIN_ID:
        if command.args is None:
            image_caption = f"Выберите свою карту дня на {datetime.today().strftime('%d.%m.%Y')}!"
        else:
            image_caption = f"Выберите свою карту дня на {datetime.today().strftime('%d.%m.%Y')}!\n{command.args}"
        image = './cards/cards.gif'
        await bot.send_animation(chat_id=config.TARGET_CHANNEL, animation=FSInputFile(image), caption=image_caption, reply_markup=start_card_of_day)


async def get_layout(message: Message, bot=Bot):
    if message.from_user.id in config.ADMIN_ID:    
        message_text = get_layout_from_db()
        await bot.send_photo(config.TARGET_CHANNEL, photo=message_text[1], caption=message_text[0], reply_markup=layout_inline())


async def admin_panel(message: Message, bot=Bot):
    if message.from_user.id in config.ADMIN_ID:
        await bot.send_message(message.from_user.id, 'Панель администратора', reply_markup=admin_panel_inline())
    else:
        await bot.send_message(message.from_user.id, 'У вас нет доступа к админке!', reply_markup=reply_keyboard_user)

async def get_horoscope(message: Message, bot=Bot):
    if message.from_user.id in config.ADMIN_ID:
        await bot.send_message(chat_id=config.TARGET_CHANNEL, text=f"Привет. Посмотри гороскоп по своему знаку зодиака на {datetime.today().strftime('%d.%m.%Y')}", reply_markup=get_zodiac_keyboard())


# --------Изменение описания карт--------
async def edit_card_desc(message: Message, state: FSMContext, bot: Bot):
    from core.handlers.callback import UpdateBigCard
    await state.update_data(description=message.text)
    data = await state.get_data()
    update_card_desc(new_desc=data['description'], card_id=data['card_id'])
    await bot.send_message(message.from_user.id, 'Описание карты изменено!', reply_markup=edit_cards_arcans_kb())





async def layout_change(message: Message, state: FSMContext):
    if message.from_user.id in config.ADMIN_ID:
        await state.set_state(Layout.title)
        await message.answer('Введите название расклада!')

async def layout_title(message: Message, state: FSMContext):
    if message.from_user.id in config.ADMIN_ID:
        await state.update_data(layout_title=message.text)
        await state.set_state(Layout.image)
        await message.answer('Прикрепите картинку!')

async def layout_image(message: Message, state: FSMContext):
    if message.from_user.id in config.ADMIN_ID:
        largest_photo = max(message.photo, key=lambda photo: photo.file_size)
        await state.update_data(image_id=largest_photo.file_id)
        await message.answer('Изображение сохранено.')
        await state.set_state(Layout.layout_context)
        await message.answer('Опишите расклады')

async def layout_context(message: Message, state: FSMContext):
    if message.from_user.id in config.ADMIN_ID:
        message_text = message.text.split('\n')
        lines = [line.strip() for line in message_text if line.strip()]
        await state.update_data(layout_context=lines)
        data = await state.get_data()
        print(data['layout_title'] + " " + data['image_id'] + " " + str(data['layout_context']))
        save_new_layout(title=data['layout_title'], image_id=data['image_id'], layout_context=data['layout_context'])
        await message.answer('Сохранено')
