from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def get_keyboard():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    first_button = KeyboardButton('Заведение с ценником в 2500р')
    second_button = KeyboardButton('Перейти на другой ресторан')
    keyboard.add(first_button, second_button)
    return keyboard

def get_keyboard_2():
    keyboard_2 = ReplyKeyboardMarkup(resize_keyboard=True)
    third_button = KeyboardButton('Заведение с ценником в 5000р')
    fourth_button = KeyboardButton('Перейти на другой ресторан')
    keyboard_2.add(third_button, fourth_button)
    return keyboard_2

def get_keyboard_3():
    keyboard_3 = ReplyKeyboardMarkup(resize_keyboard=True)
    fifth_button = KeyboardButton('Заведение с ценником от 5000 тысяч и выше')
    sixth_button = KeyboardButton('Вернуться назад')
    keyboard_3.add(fifth_button, sixth_button)
    return keyboard_3