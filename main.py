from aiogram.utils import executor
from handlers import dp
from data_base.SQLite import check_connection


async def on_startup(_):
    print('Бот запущен')
    try:
        check_connection()
        print('Подключение к БД успешное!')
    except:
        print('Ошибка БД')



if __name__ == '__main__':
    executor.start_polling(dispatcher=dp, skip_updates=True, on_startup=on_startup)
