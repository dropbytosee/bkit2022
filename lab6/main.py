from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


markup = ReplyKeyboardMarkup(resize_keyboard=True).add(
    KeyboardButton('Изменить'),
    KeyboardButton('Просмотр'),
    KeyboardButton('Удалить')
)

global_state = {}


class UserState(StatesGroup):
    name = State()
    phone = State()
    address = State()


bot = Bot(token='5752411460:AAG25_WOjneNgmMBjkDfp16BGG0Yyyh9xRQ')

storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


@dp.message_handler(text=['Изменить'])
async def change(message: types.Message):
    await message.answer("Введите ваше имя.")
    await UserState.name.set()


@dp.message_handler(text=['Просмотр'])
async def change(message: types.Message):
    if global_state:
        await message.answer(f"Имя: {global_state['username']}\n"
                             f"Телефон: {global_state['phone']}\n"
                             f"Адрес: {global_state['address']}", reply_markup=markup)
    else:
        await message.answer('Вы не заполнили форму!', reply_markup=markup)


@dp.message_handler(text=['Удалить'])
async def delete(message: types.Message):
    global global_state
    global_state = {}
    await message.answer("Данные были удалены!", reply_markup=markup)


@dp.message_handler(commands=['start'])
async def user_register(message: types.Message):
    await message.answer("Здравствуйте! Для взаимодействия с ботом используйте кнопки", reply_markup=markup)


@dp.message_handler(state=UserState.name)
async def get_username(message: types.Message, state: FSMContext):
    await state.update_data(username=message.text)
    await message.answer("Отлично! Теперь введите ваш номер телефона.")
    await UserState.next()


@dp.message_handler(state=UserState.phone)
async def get_username(message: types.Message, state: FSMContext):
    await state.update_data(phone=message.text)
    await message.answer("Отлично! Теперь введите ваш адрес.")
    await UserState.next()


@dp.message_handler(state=UserState.address)
async def get_address(message: types.Message, state: FSMContext):
    global global_state
    await state.update_data(address=message.text)
    data = await state.get_data()
    await message.answer(f"Имя: {data['username']}\n"
                         f"Телефон: {data['phone']}\n"
                         f"Адрес: {data['address']}", reply_markup=markup)
    global_state = await state.get_data()
    await state.finish()


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=False)

