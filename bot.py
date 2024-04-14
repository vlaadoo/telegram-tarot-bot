import config
from core.handlers.basic import cmd_start, get_day_card, get_layout, admin_panel, \
    layout_title, layout_image, layout_1, layout_2, layout_3, Layout
from core.handlers.callback import select_card_of_day, stop_card_of_day_handler, change_layout, \
    layout_1_call, layout_2_call, layout_3_call
from core.utils.commands import set_command

import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram import F

from pyrogram import Client, idle, filters
from pyrogram.types import Message
from pyrogram.handlers import MessageHandler

async def start_bot(bot: Bot):
    await set_command(bot)

async def new_post(client: Client, message: Message):
    await client.copy_message(chat_id=config.TECH_CHANNEL, from_chat_id=message.chat.id, message_id=message.id)

async def copy_to_my_channel(client: Client, message: Message):
    await client.copy_message(chat_id=config.TARGET_CHANNEL, from_chat_id=message.chat.id, message_id=message.reply_to_message_id)
    await client.delete_messages(chat_id=config.TECH_CHANNEL, message_ids=[message.id, message.reply_to_message_id])

async def main():
    bot = Bot(token=config.TOKEN)
    dp = Dispatcher()
    dp.startup.register(start_bot)

    dp.message.register(cmd_start, Command(commands=['start', 'run']))
    dp.message.register(get_day_card, Command(commands=['card']))
    dp.message.register(get_layout, Command(commands=['layout']))
    dp.message.register(admin_panel, Command(commands=['admin']))
    
    dp.callback_query.register(select_card_of_day, F.data.startswith('select_card_of_day'))
    dp.callback_query.register(stop_card_of_day_handler, F.data.startswith('stop_card_of_day'))
    dp.callback_query.register(change_layout, F.data.startswith('set_layout_title'))
    dp.callback_query.register(layout_1_call, F.data.startswith('layout_1_call'))
    dp.callback_query.register(layout_2_call, F.data.startswith('layout_2_call'))
    dp.callback_query.register(layout_3_call, F.data.startswith('layout_3_call'))
    
    dp.message.register(layout_title, Layout.title)
    dp.message.register(layout_image, Layout.image)
    dp.message.register(layout_1, Layout.layout_1_context)
    dp.message.register(layout_2, Layout.layout_2_context)
    dp.message.register(layout_3, Layout.layout_3_context)
        
    await dp.start_polling(bot)
    
    user_bot = Client(name='user_bot', api_id=config.API_ID, api_hash=config.API_HASH)
    bot_content = Client(name='bot_content', api_id=config.API_ID, api_hash=config.API_HASH, bot_token=config.TOKEN)

    user_bot.add_handler(MessageHandler(new_post, filters.chat(chats=config.DONOR_IDS)))
    bot_content.add_handler(MessageHandler(copy_to_my_channel, filters.reply))

    await user_bot.start()
    await bot_content.start()
    await idle()
    await user_bot.stop()
    await bot_content.stop()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')