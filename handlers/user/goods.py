from loader import dp
from aiogram.types import CallbackQuery, Message, InputFile, InputMediaPhoto, InputMedia
from keyboards import kb_main_menu, menu_data, create_goods_menu
from data_base.SQLite import get_item


@dp.callback_query_handler(menu_data.filter(menu='main'))
async def shirts(call: CallbackQuery):
    current_id = 0
    current_item = call.data.split(':')[-1]
    cur_product = get_item(current_item)
    photo = InputFile(path_or_bytesio=cur_product[current_id][2])
    # name = call.message.from_user.full_name
    current_chat_id = call.message.chat.id
    current_message_id = call.message.message_id
    caption = f"{cur_product[current_id][3]}\n{cur_product[current_id][4]}\n\n" \
              f"Стоимость: {cur_product[current_id][6]}"
    await dp.bot.edit_message_media(media=InputMediaPhoto(media=photo,
                                                          caption=caption),
                                    chat_id=current_chat_id,
                                    message_id=current_message_id,
                                    reply_markup=create_goods_menu(current_id, current_item, 0))