from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from .callback import main_menu

kb_main_menu = InlineKeyboardMarkup(row_width=2)

btn_jackets = InlineKeyboardButton(text='Куртки',
                                   callback_data=main_menu.new(menu='main',
                                                               item='jacket'))
btn_shirt = InlineKeyboardButton(text='Рубашки',
                                 callback_data=main_menu.new(menu='main',
                                                             item='shirt'))
btn_jeans = InlineKeyboardButton(text='Джинсы',
                                 callback_data=main_menu.new(menu='main',
                                                             item='jeans'))
btn_shoes = InlineKeyboardButton(text='Обувь',
                                 callback_data=main_menu.new(menu='main',
                                                             item='shoes'))

btn_basket = InlineKeyboardButton(text='Корзина',
                                  callback_data=main_menu.new(menu='basket',
                                                              item=''))

kb_main_menu.row(btn_jackets, btn_shirt, btn_jeans, btn_shoes)
kb_main_menu.row(btn_basket)