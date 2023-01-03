from loader import dp
from data_base.db_variable import db_var
from data_base.SQLite import new_item, get_item
from aiogram.types import Message, InputFile, CallbackQuery, InputMediaPhoto, InputMedia
from keyboards import kb_main_menu, navi_goods


@dp.message_handler(commands=['new'])
async def com_start(message: Message):
    for good in db_var:
        new_item(db_var.get(good))