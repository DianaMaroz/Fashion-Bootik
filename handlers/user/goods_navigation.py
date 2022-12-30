from loader import dp
from aiogram.types import CallbackQuery, Message, InputFile, InputMediaPhoto, InputMedia
from keyboards import kb_main_menu, menu_data, navi_goods, create_goods_menu
from data_base.db_variable import db_var


@dp.callback_query_handler(navi_goods.filter(menu='goods'))
async def navi_goods(call: CallbackQuery):
    print(call.data)
    current_id = int(call.data.split(':')[-1])
    current_item = call.data.split(':')[-2]
    cur_product = {}
    for product in db_var.values():
        if product.get('type') == current_item and product.get('id') == current_id:
            cur_product = product
    print(cur_product)
    photo = InputFile(path_or_bytesio=cur_product.get('image'))
    name = call.message.from_user.full_name
    current_chat_id = call.message.chat.id
    current_message_id = call.message.message_id
    caption = f"{cur_product.get('name')}\n{cur_product.get('description')}\n\n" \
              f"Размеры: {cur_product.get('size')}\nСтоимость: {cur_product.get('price')}"
    await dp.bot.edit_message_media(media=InputMediaPhoto(media=photo,
                                                          caption=caption),
                            chat_id=current_chat_id,
                            message_id=current_message_id,
                            reply_markup=create_goods_menu(current_id, current_item))