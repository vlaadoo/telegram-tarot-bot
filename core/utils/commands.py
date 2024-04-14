from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault

async def set_command(bot: Bot):
    commands = [
        BotCommand(command="/start", description="Запустить бота"),
        BotCommand(command="/card", description="Получить карту дня"),
        BotCommand(command="/layout", description="Получить расклад"),
    ]
    
    await bot.set_my_commands(commands, BotCommandScopeDefault())