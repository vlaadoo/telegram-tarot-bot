import config
from core.handlers.basic import cmd_start, get_day_card, get_layout, admin_panel, \
    Layout, get_horoscope, \
    edit_card_desc, layout_context, layout_image, layout_title
from core.handlers.callback import select_card_of_day, change_layout, \
    layout_call, \
    edit_cards, edit_big_arcans, edit_pentacli, edit_zhezly, edit_mechi, edit_chashi, \
    get_horoscope_call, edit_card_id, UpdateBigCard, \
    show_cards, show_big_arcans, show_pentacli, show_zhezly, show_mechi, show_chashi, show_card_details, \
    select_card_of_day_2
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
    dp.message.register(get_horoscope, Command(commands=['horoscope']))
    dp.callback_query.register(admin_panel, F.data.startswith('adminka'))
    
    dp.callback_query.register(select_card_of_day, F.data.startswith('select_card_of_day'))
    dp.callback_query.register(select_card_of_day_2, F.data.startswith('2_select_card_of_day'))

    dp.callback_query.register(layout_call, F.data.regexp("^layout_\d_call$"))
    dp.callback_query.register(get_horoscope_call, F.data.startswith('aries') | F.data.startswith('taurus') 
        | F.data.startswith('gemini') | F.data.startswith('cancer') | F.data.startswith('leo') | F.data.startswith('virgo') 
        | F.data.startswith('libra') | F.data.startswith('scorpio') | F.data.startswith('sagittarius') 
        | F.data.startswith('capricorn') | F.data.startswith('aquarius') | F.data.startswith('pisces'))
    
    
    dp.callback_query.register(change_layout, F.data.startswith('my_change_layout'))
    dp.message.register(layout_title, Layout.title)
    dp.message.register(layout_image, Layout.image)
    dp.message.register(layout_context, Layout.layout_context)
        
    # Изменение описания карт
    dp.callback_query.register(edit_cards, F.data.startswith('change_cards'))
    dp.callback_query.register(edit_big_arcans, F.data.startswith('big_arcans'))
    dp.callback_query.register(edit_pentacli, F.data.startswith('pentacli'))
    dp.callback_query.register(edit_zhezly, F.data.startswith('zhezly'))
    dp.callback_query.register(edit_mechi, F.data.startswith('mechi'))
    dp.callback_query.register(edit_chashi, F.data.startswith('chashi'))
    
    dp.callback_query.register(edit_card_id, F.data.regexp("^([0-6]?[0-9]|7[0-7])$"))
    dp.message.register(edit_card_desc, UpdateBigCard.description)
    
    dp.callback_query.register(show_cards, F.data.startswith('check_cards'))
    dp.callback_query.register(show_big_arcans, F.data.startswith('check_big_arcans'))
    dp.callback_query.register(show_pentacli, F.data.startswith('check_pentacli'))
    dp.callback_query.register(show_zhezly, F.data.startswith('check_zhezly'))
    dp.callback_query.register(show_mechi, F.data.startswith('check_mechi'))
    dp.callback_query.register(show_chashi, F.data.startswith('check_chashi'))
    dp.callback_query.register(show_card_details, F.data.regexp("^([0-6]?[0-9]|7[0-7])_check$"))
    
    
    
    
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