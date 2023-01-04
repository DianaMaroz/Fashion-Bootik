from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from .callback import menu_data, navi_goods
from data_base.db_variable import db_var
from data_base.SQLite import get_item, get_by_id, get_basket

def create_basket_kb(id_user: int):
    kb_goods = InlineKeyboardMarkup(row_width=1)
    my_basket = get_basket(id_user)
    if len(my_basket) != 0:
        for i in range(len(my_basket)):
            goods = f'Удалить {get_by_id(int(my_basket[i][-1]))[3]}'
            kb_goods.add(InlineKeyboardButton(text=goods,
                                  callback_data=navi_goods.new(
                                      menu='remove', user_id='0',
                                      goods_id='0', item='0',
                                      id=get_by_id(int(my_basket[i][-1]))[0])))
    btn_back = InlineKeyboardButton(text='Назад в главное меню',
                                    callback_data=navi_goods.new(
                                        menu='back', user_id='0',
                                        goods_id='0', item='0',
                                        id='0'))

    kb_goods.add(btn_back)
    return kb_goods