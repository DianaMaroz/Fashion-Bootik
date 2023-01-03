from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from .callback import menu_data
from data_base.SQLite import get_item

kb_main_menu = InlineKeyboardMarkup(row_width=2)

btn_jackets = InlineKeyboardButton(text='Куртки',
                                   callback_data=menu_data.new(menu='main',
                                                               item='jacket'))
btn_shirt = InlineKeyboardButton(text='Рубашки',
                                 callback_data=menu_data.new(menu='main',
                                                             item='shirt'))
btn_jeans = InlineKeyboardButton(text='Джинсы',
                                 callback_data=menu_data.new(menu='main',
                                                             item='jeans'))
btn_shoes = InlineKeyboardButton(text='Обувь',
                                 callback_data=menu_data.new(menu='main',
                                                             item='shoes'))

btn_basket = InlineKeyboardButton(text='Корзина',
                                  callback_data=menu_data.new(menu='basket',
                                                              item=''))

kb_main_menu.row(btn_jackets, btn_shirt, btn_jeans, btn_shoes)
kb_main_menu.row(btn_basket)

