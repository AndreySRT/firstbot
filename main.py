from aiogram import Bot, Dispatcher, executor, types
from config import telegram_token
from keyboard.keyboards import get_keyboard, get_keyboard_2, get_keyboard_3
from keyboard.key_inline import get_keyboard_inline, get_keyboard_inline_2, get_keyboard_inline_3


bot = Bot(token = telegram_token)
dp = Dispatcher(bot)

async def set_commands(bot: Bot):
    commands = [
    types.BotCommand(command='/start', description='Комманда для того, чтобы запустить бота'),
    types.BotCommand(command='/help', description='Комманда для того, чтобы узнать, с чем может помочь наш бот'),
    types.BotCommand(command='/info', description='Комманда для того, чтобы узнать полную информацию о боте'),
    types.BotCommand(command='/chatbot', description='Комманда для того, чтобы поболтать со мной'),
    types.BotCommand(command='/botplay', description='Комманда для того, чтобы сыграть со мной и проверить свои знания')
]  #Создание массива комманд

    await bot.set_my_commands(commands) #Передаем массив комманд в бота


@dp.message_handler(commands='start')
async def start(message: types.Message):
    await message.answer('Привет! Я твой персональный бот и друг, я помогу тебе с выбором шикарного ресторана за любую цену.', reply_markup=get_keyboard())  #Можно использовать тег reply но он будет пересылать твое сообщение, после писать твое сообщение.

@dp.message_handler(lambda message: message.text == 'Заведение с ценником в 2500р')
async def first_button_click(message: types.message):
    await bot.send_photo(message.chat.id, photo= 'https://i4.photo.2gis.com/images/branch/0/30258560074423042_ebc5.jpg', caption='Эти два ресторана предоставляют общирный вид пищи за небольшую цену', reply_markup=get_keyboard_inline())
    #await message.answer('Ты нажал кнопку 1')

@dp.message_handler(lambda message: message.text == 'Перейти на другой ресторан')
async def second_button_click(message: types.message):
    await message.answer('Тут ты можешь посмотреть на рестораны с видом на Москву-реку', reply_markup=get_keyboard_2())

@dp.message_handler(lambda message: message.text == 'Заведение с ценником в 5000р')
async def third_button_click(message: types.message):
    await bot.send_photo(message.chat.id, photo= 'https://image.eatout.ru/imager/0000/0000/0000/0500/0501/1100x/5000501.jpeg', caption='Вот и еще ресторан, который предоставляет общирный выбор тот же вид пищи только в цетре Москвы', reply_markup=get_keyboard_inline_2())

@dp.message_handler(lambda message: message.text == 'Перейти на другой ресторан')
async def fourth_button_click(message: types.message):
    await message.answer('Тут ты можешь посмотреть на рестораны который любезно нам представила Москва-сити', reply_markup=get_keyboard_3())

@dp.message_handler(lambda message: message.text == 'Заведение с ценником от 5000 тысяч и выше')
async def fifth_button_click(message: types.message):
    await bot.send_photo(message.chat.id, photo= 'https://static.tildacdn.com/tild6366-3762-4266-a533-636235393964/7.jpg', caption='Вот и еще ресторан, который предоставляет общирный выбор тот же вид пищи только в цетре Москвы и в Москва-сити', reply_markup=get_keyboard_inline_3())

@dp.message_handler(lambda message: message.text == 'Вернуться назад')
async def sixth_button_click(message: types.message):
    await message.answer('Тут ты можешь посмотреть на рестораны окутанные Москвой-рекой', reply_markup=get_keyboard())

@dp.message_handler(commands='help')
async def help(message: types.Message):
    await message.reply('Если у тебя возникли вопросы или проблемы при использовании бота, не стесняйся обращаться ко мне.')

@dp.message_handler(commands='info')
async def info(message: types.Message):
    await message.answer('Привет! Я - твой персональный бот, готовый помочь с различными задачами. Я обучен выполнять разнообразные команды, от предоставления информации до выполнения действий по твоему запросу. Просто напиши мне, что тебе нужно, и я постараюсь помочь.')

@dp.message_handler(commands='chatbot')
async def chatbot(message: types.Message):
    await message.answer('Если тебе наскучит, я могу с тобой поболтать на любую свободную тему чтобы разрядить обстановку.')

@dp.message_handler(commands='botplay')
async def botplay(message: types.Message):
    await message.answer('Давай поиграем в угадайку: задавай мне вопросы, а я буду отвечать "да" или "нет"')

@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)

async def on_startup(dispatcher): #Вызываем нашу функцию
    await set_commands(dispatcher.bot)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)