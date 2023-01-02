from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from .callback import menu_data, navi_goods
from data_base.db_variable import db_var
from data_base.SQLite import get_item

def create_goods_menu(cur_id: int, item: str):
    goods = get_item(item)
    # for product in db_var.values():
    #     if product.get('type') == item:
    #         goods.append(item)
    # for i in goods:
    #     print(i)
    current_id = cur_id
    next_id = cur_id + 1
    prev_id = cur_id - 1
    if current_id == 1:
        prev_id = len(goods)
    elif current_id == len(goods):
        next_id = 1
    kb_goods = InlineKeyboardMarkup(row_width=1)

    btn_buy = InlineKeyboardButton(text='Купить',
                                  callback_data=navi_goods.new(
                                      menu='goods',
                                      item=item,
                                  id=current_id))
    btn_prev = InlineKeyboardButton(text='<<<',
                                   callback_data=navi_goods.new(
                                       menu='goods',
                                       item=item,
                                   id=prev_id))
    btn_next = InlineKeyboardButton(text='>>>',
                                   callback_data=navi_goods.new(
                                       menu='goods',
                                       item=item,
                                       id=next_id))
    btn_back = InlineKeyboardButton(text='Назад в главное меню',
                                    callback_data=navi_goods.new(
                                        menu='back',
                                        item=item,
                                        id=next_id))

    kb_goods.row(btn_prev, btn_buy, btn_next)
    kb_goods.add(btn_back)
    return kb_goods
