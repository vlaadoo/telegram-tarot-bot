from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


start_card_of_day = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text="Выбрать карту",
            callback_data="select_card_of_day"
        )
    ]
])

stop_card_of_day = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text="Остановить", 
            callback_data="stop_card_of_day"
        )
    ]
])

admin_panel_inline = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text="Выбрать название расклада",
            callback_data="set_layout_title"
        )
        # InlineKeyboardButton(
        #     text="Изменить ответы",
        #     callback_data="change_layout_answers"
        # ),
    ]
])


layout_inline = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="1", callback_data="layout_1_call"),
        InlineKeyboardButton(text="2", callback_data="layout_2_call"),
        InlineKeyboardButton(text="3", callback_data="layout_3_call"),
    ]
])