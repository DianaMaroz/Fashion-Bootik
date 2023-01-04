from loader import dp
from aiogram.types import Message, InputFile, CallbackQuery, InputMediaPhoto, InputMedia
from keyboards import kb_main_menu, navi_goods


@dp.callback_query_handler(navi_goods.filter(menu='back'))
async def com_start(call: CallbackQuery):
    photo = InputFile('images/logo.png')
    name = call.message.from_user.full_name
    current_chat_id = call.message.chat.id
    current_message_id = call.message.message_id
    caption = f'{name}, добро пожаловать в онлайн бутик!'
    await dp.bot.edit_message_media(media=InputMediaPhoto(media=photo,
                                                          caption=caption),
                                    chat_id=current_chat_id,
                                    message_id=current_message_id,
                                    reply_markup=kb_main_menu)


@dp.message_handler(commands=['start'])
async def com_start(message: Message):
    photo = InputFile('images/logo.png')
    name = message.from_user.full_name
    chat_id = message.chat.id
    await dp.bot.send_photo(chat_id=chat_id,
                            photo=photo,
                            caption=f'{name}, добро пожаловать в онлайн бутик!',
                            reply_markup=kb_main_menu)


@dp.message_handler(commands=['me'])
async def my_id(message: Message):
    await message.answer(text=message.from_user.id)