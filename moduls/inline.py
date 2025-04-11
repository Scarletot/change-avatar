from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="міні-бари", callback_data="minibar")],
        [InlineKeyboardButton(text="клаб лаунж", callback_data="club")],
        [InlineKeyboardButton(text="олівера", callback_data="olivera")],
        [InlineKeyboardButton(text="вихідний", callback_data="weekend")],
        [InlineKeyboardButton(text="коледж", callback_data="college")],
        [InlineKeyboardButton(text="добавити своє", callback_data="option")],
    ]
)
