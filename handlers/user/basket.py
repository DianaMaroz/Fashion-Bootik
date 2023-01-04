from loader import dp
from aiogram.types import CallbackQuery, Message, InputFile, InputMediaPhoto, InputMedia
from keyboards import kb_main_menu, menu_data, navi_goods, create_goods_menu
from data_base.SQLite import get_item, add_to_basket, set_count, get_basket, get_by_id
from keyboards import create_basket_kb


@dp.callback_query_handler(navi_goods.filter(menu='basket'))
async def navi_goods(call: CallbackQuery):
    id_user = call.from_user.id
    id_goods = int(call.data.split(":")[-3])
    if set_count(id_goods, -1):
        await call.answer(f'Товар {id_goods} добавлен в корзину')
        add_to_basket(id_user, id_goods)
    else:
        await call.answer(f'Извините, но товара нет в наличии', show_alert=True)


@dp.callback_query_handler(menu_data.filter(menu='basket'))
async def navi_goods(call: CallbackQuery):
    id_user = call.from_user.id
    current_message_id = call.message.message_id
    my_basket = get_basket(id_user)
    content_basket = 'Содержимое вашей корзины:\n'
    total = 0
    if len(my_basket) != 0:
        for i in range(len(my_basket)):
            goods_id = int(my_basket[i][-1])
            goods = get_by_id(goods_id)
            content_basket += f'{i+1}. {goods[3]}\n'
            total += float(goods[-1])
        content_basket += f'Общая сумма: {total} рублей'
    else:
        content_basket += 'Пусто'
    photo = InputFile('images/logo.png')
    await dp.bot.edit_message_media(media=InputMediaPhoto(media=photo,
                                                          caption=content_basket),
                                    chat_id=id_user,
                                    message_id=current_message_id,
                                    reply_markup=create_basket_kb(id_user))