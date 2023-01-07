from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from loader import db
from .callback import main_menu, navigation


def create_basket_kb(id_user: int):
    kb_goods = InlineKeyboardMarkup(row_width=1)
    my_basket = db.get_basket(id_user=id_user)
    if len(my_basket) != 0:
        for i in range(len(my_basket)):
            id_order = str(my_basket[i][0])
            id_user = str(my_basket[i][1])
            id_goods = str(my_basket[i][2])
            goods = db.get_goods(id=id_goods)
            name_goods = goods[0][3]
            item_menu = f'Удалить {name_goods}'
            kb_goods.add(InlineKeyboardButton(text=item_menu,
                                              callback_data=navigation.new(
                                                  menu='remove', user_id=id_user,
                                                  goods_id=id_goods, item=id_order,
                                                  id=id_order)))
    btn_back = InlineKeyboardButton(text='Назад в главное меню',
                                    callback_data=main_menu.new(
                                        menu='back', item=''))

    kb_goods.add(btn_back)
    return kb_goods
