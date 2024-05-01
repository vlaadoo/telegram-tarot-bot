from aiogram import Bot
from aiogram.types import Message, FSInputFile
from aiogram.filters import CommandObject
from core.keyboards.inline import start_card_of_day, layout_inline, get_zodiac_keyboard
import config
from core.database.database import get_layout_from_db



from datetime import datetime

async def moder_get_day_card(message: Message, command: CommandObject, bot=Bot):
    if message.from_user.id in config.ADMIN_ID:
        if command.args is None:
            image_caption = f"Выберите свою карту дня на {datetime.today().strftime('%d.%m.%Y')}!"
        else:
            image_caption = f"Выберите свою карту дня на {datetime.today().strftime('%d.%m.%Y')}!\n{command.args}"
        image = './cards/cards.gif'
        await bot.send_animation(chat_id=config.TECH_CHANNEL, animation=FSInputFile(image), caption=image_caption, reply_markup=start_card_of_day)


async def moder_get_layout(message: Message, bot=Bot):
    if message.from_user.id in config.ADMIN_ID:    
        message_text = get_layout_from_db()
        await bot.send_photo(config.TECH_CHANNEL, photo=message_text[1], caption=message_text[0], reply_markup=layout_inline())


async def moder_get_horoscope(message: Message, bot=Bot):
    if message.from_user.id in config.ADMIN_ID:
        await bot.send_message(chat_id=config.TECH_CHANNEL, text=f"Привет. Посмотри гороскоп по своему знаку зодиака на {datetime.today().strftime('%d.%m.%Y')}", reply_markup=get_zodiac_keyboard())