from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from data_base.SQLite import new_item
from loader import dp
from aiogram.types import Message
from keyboards import kb_g_type
from config import admin



class NewGoodsItem(StatesGroup):
    name = State()
    desc = State()
    g_type = State()
    photo = State()
    quantity = State()
    price = State()



@dp.message_handler(commands=['add'], state=None)
async def add_catch(message: Message):
    access = False
    for user_id in admin:
        if message.from_user.id == user_id:
            access = True
            break
    if access:
        await message.answer('Введите название товара')
        await NewGoodsItem.name.set()
    else:
        await message.answer('Извините, у вас нет доступа к этой команде')

@dp.message_handler(state=NewGoodsItem.name)
async def name_catch(message: Message, state: FSMContext):
    await state.update_data({'name': message.text})
    await message.answer('Введите описание товара')
    await NewGoodsItem.next()

@dp.message_handler(state=NewGoodsItem.desc)
async def desc_catch(message: Message, state: FSMContext):
    await state.update_data({'desc': message.text})
    await message.answer('Введите тип товара', reply_markup=kb_g_type)
    await NewGoodsItem.next()


@dp.message_handler(state=NewGoodsItem.g_type)
async def type_catch(message: Message, state: FSMContext):
    if message.text in ['jacket', 'shirt', 'jeans', 'shoes']:
        await state.update_data({'g_type': message.text})
        await message.answer('Введите фото товара')
        await NewGoodsItem.next()
    else:
        await message.answer('Выберите категорию из списка', reply_markup=kb_g_type)

@dp.message_handler(content_types='photo', state=NewGoodsItem.photo)
async def photo_catch(message: Message, state: FSMContext):
    await state.update_data({'image': message.photo[0].file_id})
    await message.answer('Введите количество товара')
    await NewGoodsItem.next()

@dp.message_handler(state=NewGoodsItem.quantity)
async def quantity_catch(message: Message, state: FSMContext):
    await state.update_data({'quantity': message.text})
    await message.answer('Введите цену товара')
    await NewGoodsItem.next()

@dp.message_handler(state=NewGoodsItem.price)
async def price_catch(message: Message, state: FSMContext):
    await state.update_data({'price': message.text})
    data = await state.get_data()
    try:
        new_item(data)
        await message.answer(f'Товар {data.get("name")} добавлен!')
    except:
        await message.answer(f'Ошибка! добавления товара! Проверьте правильность вводимых данных')
    await state.reset_data()
    await state.finish()
