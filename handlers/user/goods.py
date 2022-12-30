from loader import dp
from aiogram.types import CallbackQuery, Message, InputFile, InputMediaPhoto, InputMedia
from keyboards import kb_main_menu, menu_data, create_goods_menu


@dp.callback_query_handler(menu_data.filter(menu='main'))
async def shirts(call: CallbackQuery):

    name = call.message.from_user.full_name
    current_chat_id = call.message.chat.id
    current_message_id = call.message.message_id
    if call.data.split(':')[-1] == 'shirt':
        photo = InputFile(path_or_bytesio='images/shirt/shirt_1.jpg')
        await dp.bot.edit_message_media(media=InputMediaPhoto(media=photo,
                                                              caption='Рубашка'),
                                chat_id=current_chat_id,
                                message_id=current_message_id,
                                reply_markup=create_goods_menu(1, 'shirt'))
    if call.data.split(':')[-1] == 'jacket':
        photo = InputFile(path_or_bytesio='images/jacket/jacket_1.jpg')
        await dp.bot.edit_message_media(media=InputMediaPhoto(media=photo,
                                                              caption='Куртки'),
                                chat_id=current_chat_id,
                                message_id=current_message_id,
                                reply_markup=create_goods_menu(1, 'jacket'))
    if call.data.split(':')[-1] == 'jeans':
        photo = InputFile(path_or_bytesio='images/jeans/jeans_1.jpg')
        await dp.bot.edit_message_media(media=InputMediaPhoto(media=photo,
                                                              caption='Джинсы'),
                                chat_id=current_chat_id,
                                message_id=current_message_id,
                                reply_markup=create_goods_menu(1, 'jeans'))
    if call.data.split(':')[-1] == 'shoes':
        photo = InputFile(path_or_bytesio='images/shoes/shoes_1.jpg')
        await dp.bot.edit_message_media(media=InputMediaPhoto(media=photo,
                                                              caption='Обувь'),
                                chat_id=current_chat_id,
                                message_id=current_message_id,
                                reply_markup=create_goods_menu(1, 'shoes'))