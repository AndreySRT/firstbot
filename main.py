from aiogram import Bot, Dispatcher, executor, types
from config import telegram_token

bot = Bot(token = telegram_token)
dp = Dispatcher(bot)

async def set_commands(bot: Bot):
    commands = [
    types.BotCommand(command='/start', description='Комманда для того, чтобы запустить бота'),
    types.BotCommand(command='/help', description='Комманда для того, чтобы узнать, с чем может помочь наш бот'),
    types.BotCommand(command='/info', description='Комманда для того, чтобы узнать полную информацию о боте')
]  #Создание массива комманд

    await bot.set_my_commands(commands) #Передаем массив комманд в бота

@dp.message_handler(commands='start')
async def start(message: types.Message):
    await message.answer('Привет, Бонжур, Хеллоу!')  #Можно использовать тег reply но он будет пересылать твое сообщение, после писать твое сообщение.

@dp.message_handler(commands='help')
async def help(message: types.Message):
    await message.reply('Если у тебя возникли вопросы или проблемы при использовании бота, не стесняйся обращаться ко мне.')

@dp.message_handler(commands='info')
async def info(message: types.Message):
    await message.answer('Привет! Я - твой персональный бот, готовый помочь с различными задачами. Я обучен выполнять разнообразные команды, от предоставления информации до выполнения действий по твоему запросу. Просто напиши мне, что тебе нужно, и я постараюсь помочь.')

@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)

async def on_startup(dispatcher): #Вызываем нашу функцию
    await set_commands(dispatcher.bot)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)