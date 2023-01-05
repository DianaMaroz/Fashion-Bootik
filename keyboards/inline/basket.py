from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from loader import db
from .callback import main_menu, navigation
from data_base.db_variable import db_var
# from data_base.SQLite import get_item, get_by_id, get_basket

def create_basket_kb(id_user: int):
    kb_goods = InlineKeyboardMarkup(row_width=1)
    my_basket = db.get_basket(id_user=id_user)
    if len(my_basket) != 0:
        for i in range(len(my_basket)):
            goods_id = int(my_basket[i][-1]))[0]))
            goods_name = get_by_id(int(my_basket[i][-1]))[3]
            goods = f'Удалить {get_by_id(int(my_basket[i][-1]))[3]}'
            kb_goods.add(InlineKeyboardButton(text=goods,
                                  callback_data=navigation.new(
                                      menu='remove', user_id='0',
                                      goods_id='0', item='0',
                                      id=get_by_id(int(my_basket[i][-1]))[0])))
    btn_back = InlineKeyboardButton(text='Назад в главное меню',
                                    callback_data=main_menu.new(
                                        menu='back', item=''))

    kb_goods.add(btn_back)
    return kb_goods