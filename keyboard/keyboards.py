from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def get_keyboard():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    first_button = KeyboardButton('Заведение с ценником в 2500р')
    second_button = KeyboardButton('Перейти на другой ресторан')
    keyboard.add(first_button, second_button)
    return keyboard

def get_keyboard_2():
    keyboard_2 = ReplyKeyboardMarkup(resize_keyboard=True)
    third_button = KeyboardButton('Заведение с ценником от 5000 тысяч и выше')
    fourth_button = KeyboardButton('Вернуться назад')
    keyboard_2.add(third_button, fourth_button)
    return keyboard_2