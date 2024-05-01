from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault

async def set_command(bot: Bot):
    commands = [
        BotCommand(command="/start", description="Запустить бота"),
        BotCommand(command="/moder_layout", description="Отправить расклад в канал для модерации"),
        BotCommand(command="/moder_card", description="Отправить карту дня в канал для модерации"),
        BotCommand(command="/moder_horoscope", description="Отправить гороскоп в канал для модерации"),
        BotCommand(command="/main", description="Ниже команды для основного канала"),
        BotCommand(command="/card", description="Получить карту дня"),
        BotCommand(command="/layout", description="Получить расклад"),
        BotCommand(command="/horoscope", description="Получить гороскоп"),
    ]
    
    await bot.set_my_commands(commands, BotCommandScopeDefault())