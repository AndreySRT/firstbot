from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def get_keyboard_inline():
    keyboard_inline = InlineKeyboardMarkup(row_width=2)
    bot_inline_1 = InlineKeyboardButton('Посмотреть', url='https://cattish.ru/breed/?ysclid=lwq86rccq0176056340')
    bot_inline_2 = InlineKeyboardButton('Посмотреть', url='https://cattish.ru/breed/?ysclid=lwq86rccq0176056340')
    keyboard_inline.add(bot_inline_1, bot_inline_2)
    return keyboard_inline