from aiogram import Bot
from aiogram.types import Message
from core.keyboards.inline import start_card_of_day, admin_panel_inline, layout_inline
from core.keyboards.reply import reply_keyboard_user
import config

from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

class Layout(StatesGroup):
    title = State()
    image = State()
    layout_1_context = State()
    layout_2_context = State()
    layout_3_context = State()

async def cmd_start(message: Message, bot=Bot):
    await message.answer(f'Привет, {message.from_user.first_name}, добро пожаловать!', reply_markup=reply_keyboard_user)


async def get_day_card(message: Message, bot=Bot):
    await bot.send_message(message.from_user.id, 'Выберите карту дня!', reply_markup=start_card_of_day)


async def get_layout(message: Message, bot=Bot):
    with open('./image.txt', 'r', encoding='utf-8') as f:
        image_url = f.readline()
    with open('./layout_title.txt', 'r', encoding='utf-8') as f:
        layout_title_file = f"{f.read()}\nВыберите расклад:"
    await bot.send_photo(message.from_user.id, image_url, caption=layout_title_file, reply_markup=layout_inline)    


async def admin_panel(message: Message, bot=Bot):
    if message.from_user.id in config.ADMIN_ID:
        await bot.send_message(message.from_user.id, 'Панель администратора', reply_markup=admin_panel_inline)
    else:
        await bot.send_message(message.from_user.id, 'У вас нет доступа к админке!', reply_markup=reply_keyboard_user)


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
        await state.set_state(Layout.layout_1_context)
        await message.answer('Опишите первый расклад')


async def layout_1(message: Message, state: FSMContext):
    if message.from_user.id in config.ADMIN_ID:
        await state.update_data(layout_1_context=message.text)
        await state.set_state(Layout.layout_2_context)
        await message.answer('Опишите второй расклад')


async def layout_2(message: Message, state: FSMContext):
    if message.from_user.id in config.ADMIN_ID:
        await state.update_data(layout_2_context=message.text)
        await state.set_state(Layout.layout_3_context)
        await message.answer('Опишите третий расклад')


async def layout_3(message: Message, state: FSMContext):
    if message.from_user.id in config.ADMIN_ID:
        await state.update_data(layout_3_context=message.text)
        await message.answer('Сохранение...')
        data = await state.get_data()
        try:
            with open('./layout_title.txt', 'w', encoding='utf-8') as f:
                f.write(data['layout_title'])
            with open('./image.txt', 'w', encoding='utf-8') as f:
                f.write(data['image_id'])
            with open('./1.txt', 'w', encoding='utf-8') as f:
                f.write(data['layout_1_context'])
            with open('./2.txt', 'w', encoding='utf-8') as f:
                f.write(data['layout_2_context'])
            with open('./3.txt', 'w', encoding='utf-8') as f:
                f.write(data['layout_3_context'])
            await message.answer('Сохранено!')
        except Exception as e:
            await message.answer(f'Ошибка: {e}')
        await state.clear()