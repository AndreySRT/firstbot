from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def get_keyboard_inline():
    keyboard_inline = InlineKeyboardMarkup(row_width=2)
    bot_inline_1 = InlineKeyboardButton('Посмотреть', url='https://cheretto-more-na-pyatnickoj.ru/?utm_source=yandex&utm_medium=cpc&utm_campaign=cheretto-more-na-pyatnickoj&utm_content=15040512867_none&utm_term=%D1%87%D0%B5%D1%80%D0%B5%D1%82%D1%82%D0%BE%20%D0%BC%D0%BE%D1%80%D0%B5&roistat=direct1_search_15040512867_%D1%87%D0%B5%D1%80%D0%B5%D1%82%D1%82%D0%BE%20%D0%BC%D0%BE%D1%80%D0%B5&roistat_referrer=none&roistat_pos=premium_1&yclid=13390972607965429759#')
    bot_inline_2 = InlineKeyboardButton('Посмотреть', url='https://mushroomsmoscow.ru/ru/?roistat=direct21_search_15045726806_mushrooms%20%D0%BC%D0%BE%D1%81%D0%BA%D0%B2%D0%B0&roistat_referrer=none&roistat_pos=premium_1&utm_source=yandex&utm_medium=cpc&utm_campaign=poisk_brand&yclid=8414297816566595583')
    keyboard_inline.add(bot_inline_1, bot_inline_2)
    return keyboard_inline

def get_keyboard_inline_2():
    keyboard_inline_2 = InlineKeyboardMarkup(row_width=2)
    bot2_inline_1 = InlineKeyboardButton('Посмотреть', url='https://butchersteak.ru/')
    bot2_inline_2 = InlineKeyboardButton('Посмотреть', url='https://www.restorating.ru/msk/catalogue/sahalin-smolenskaya-8?utm_source=yandexMoscow&utm_medium=cpc&utm_campaign=Moscow_restaurants&ref_id=1&cm_id=74891496_5250580994_14725929181_46201130425_46201130425_none_search_type1_no_desktop_premium_213&utm_content=%7Cc%3A74891496%7Cg%3A5250580994%7Cb%3A14725929181%7Ck%3A46201130425%7Cst%3Asearch%7Ca%3Ano%7Cs%3Anone%7Ct%3Apremium%7Cp%3A3%7Cr%3A46201130425%7Cdev%3Adesktop&yclid=14442383431837679615')
    keyboard_inline_2.add(bot2_inline_1, bot2_inline_2)
    return keyboard_inline_2

def get_keyboard_inline_3():
    keyboard_inline_3 = InlineKeyboardMarkup(row_width=2)
    bot3_inline_1 = InlineKeyboardButton('Посмотреть', url='https://sixtyrestaurant.ru/?utm_source=yandex&utm_medium=cpc&utm_campaign=%D0%9F%D0%BE%D0%B8%D1%81%D0%BA&utm_content=ad_a&utm_term=%D1%80%D0%B5%D1%81%D1%82%D0%BE%D1%80%D0%B0%D0%BD%D1%8B%20%D0%B2%20%D0%BC%D0%BE%D1%81%D0%BA%D0%BE%D0%B2%20%D1%81%D0%B8%D1%82%D0%B8&etext=&yclid=7711090332173336575&yadclid=105909063&yadordid=199023769')
    bot3_inline_2 = InlineKeyboardButton('Посмотреть', url='https://magma.bar/?utm_source=yandex&utm_medium=cpc&utm_campaign=111398296&utm_content=16187004022&utm_term=%D1%80%D0%B5%D1%81%D1%82%D0%BE%D1%80%D0%B0%D0%BD%D1%8B%20%D0%B2%20%D0%BC%D0%BE%D1%81%D0%BA%D0%B2%D0%B0%20%D1%81%D0%B8%D1%82%D0%B8.desktop.%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0.51988180982.none&block=premium.1&yclid=4978060503367811071')
    keyboard_inline_3.add(bot3_inline_1, bot3_inline_2)
    return keyboard_inline_3