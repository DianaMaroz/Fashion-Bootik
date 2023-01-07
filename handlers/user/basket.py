from aiogram.types import CallbackQuery, InputFile, InputMediaPhoto

from keyboards import create_basket_kb
from keyboards import main_menu, navigation
from loader import dp, db


@dp.callback_query_handler(navigation.filter(menu='basket'))
async def add_to_basket(call: CallbackQuery):
    id_user = call.from_user.id
    id_goods = int(call.data.split(":")[-1])
    goods = db.get_goods(id=id_goods)
    name_goods = goods[0][3]
    goods_quantity = db.get_goods(id=id_goods)[0][-2]
    if goods_quantity > 0:
        db.add_to_basket(id_user, id_goods)
        await call.answer(f'Товар {name_goods} добавлен в корзину')
    else:
        await call.answer(f'Извините, но {name_goods} товара нет в наличии', show_alert=True)


@dp.callback_query_handler(main_menu.filter(menu='basket'))
async def user_basket(call: CallbackQuery):
    id_user = call.from_user.id
    current_message_id = call.message.message_id
    my_basket = db.get_basket(id_user=id_user)
    content_basket = 'Содержимое вашей корзины:\n'
    total = 0
    if len(my_basket) != 0:
        for i in range(len(my_basket)):
            id_goods = int(my_basket[i][-1])
            goods = db.get_goods(id=id_goods)[0]
            content_basket += f'{i + 1}. {goods[3]}\n'
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


@dp.callback_query_handler(navigation.filter(menu='remove'))
async def remove_from_basket(call: CallbackQuery):
    id_goods = int(call.data.split(":")[-3])
    id_order = int(call.data.split(":")[-1])
    goods = db.get_goods(id=id_goods)
    name_goods = goods[0][3]
    await call.answer(f'Товар {name_goods} удален из корзины')
    db.remove_from_basket(id_order, id_goods)
    await user_basket(call)
