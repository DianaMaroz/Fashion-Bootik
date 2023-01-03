from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from .callback import menu_data, navi_goods
from data_base.db_variable import db_var
from data_base.SQLite import get_item, get_by_id

def create_goods_menu(cur_id: int, item: str, goods_id: int):
    goods = get_item(item)
    current_id = cur_id
    next_id = cur_id + 1
    prev_id = cur_id - 1
    product = get_by_id(goods_id)
    if current_id == 0:
        prev_id = len(goods) - 1
    elif current_id == len(goods) - 1:
        next_id = 0
    kb_goods = InlineKeyboardMarkup(row_width=1)

    btn_buy = InlineKeyboardButton(text='В корзину',
                                  callback_data=navi_goods.new(
                                      menu='basket', user_id='0',
                                      goods_id=goods_id, item=item,
                                      id=current_id))
    btn_prev = InlineKeyboardButton(text='<<<',
                                   callback_data=navi_goods.new(
                                       menu='goods', user_id='0',
                                       goods_id='0', item=item,
                                       id=prev_id))
    btn_next = InlineKeyboardButton(text='>>>',
                                   callback_data=navi_goods.new(
                                       menu='goods', user_id='0',
                                       goods_id='0', item=item,
                                       id=next_id))
    btn_back = InlineKeyboardButton(text='Назад в главное меню',
                                    callback_data=navi_goods.new(
                                        menu='back', user_id='0',
                                        goods_id='0', item=item,
                                        id=next_id))

    kb_goods.row(btn_prev, btn_buy, btn_next)
    kb_goods.add(btn_back)
    return kb_goods
