from aiogram.types import BotCommand, BotCommandScopeDefault


async def set_default_commands(dp):
    return await dp.bot.set_my_commands(
        commands=[
            BotCommand("start", "Начать диалог с ботом"),
            BotCommand("help", "Узнать о возможностях бота и основных командах"),
            BotCommand("report", "Отправить обратную связь по работе бота"),
        ],
        scope=BotCommandScopeDefault()
    )
