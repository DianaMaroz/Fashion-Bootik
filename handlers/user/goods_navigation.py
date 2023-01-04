from loader import dp
from aiogram.types import CallbackQuery, Message, InputFile, InputMediaPhoto, InputMedia
from keyboards import kb_main_menu, menu_data, navi_goods, create_goods_menu
from data_base.SQLite import get_item


@dp.callback_query_handler(navi_goods.filter(menu='goods'))
async def navi_goods(call: CallbackQuery):
    current_id = int(call.data.split(':')[-1])
    current_item = call.data.split(':')[-2]
    cur_product = get_item(current_item)
    goods_id = int(cur_product[current_id][0])
    if str(cur_product[current_id][2]).startswith('A'):
        photo = str(cur_product[current_id][2])
    else:
        photo = InputFile(path_or_bytesio=cur_product[current_id][2])
    current_chat_id = call.message.chat.id
    current_message_id = call.message.message_id
    caption = f"{cur_product[current_id][3]}\n{cur_product[current_id][4]}\n\n" \
              f"Стоимость: {cur_product[current_id][6]}"
    await dp.bot.edit_message_media(media=InputMediaPhoto(media=photo, caption=caption),
                                    chat_id=current_chat_id, message_id=current_message_id,
                                    reply_markup=create_goods_menu(current_id, current_item, goods_id))
