from aiogram import Dispatcher, Bot , filters, types, F
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
import asyncio
from googletrans import Translator
from aiogram.fsm.state import State , StatesGroup
from aiogram.fsm.context import FSMContext

bot = Bot(token='7015569170:AAFcDyfU3CEZj2a-Fiq3hJ1fMi_arxZgbuw')
dp = Dispatcher(bot = bot)

class Rus(StatesGroup):
    rus_text = State()
    
class Uzb(StatesGroup):
    uzb_text = State()
    
class Eng(StatesGroup):
    eng_text = State()

keyboards_translate = [
    [KeyboardButton(text='ru'),KeyboardButton(text='uz'),KeyboardButton(text='en')]
]

translate_button = ReplyKeyboardMarkup(keyboard=keyboards_translate,resize_keyboard=True)        
translator = Translator()


@dp.message(filters.Command("start"))
async def start_function(message: types.Message):
    await message.answer('til tanlang',reply_markup=translate_button)
    
    

    
    
@dp.message(F.text == 'uz')
async def uz_function(message: types.Message, state: FSMContext):
    await state.set_state(Uzb.uzb_text)
    await message.answer('text kiriting')
    
@dp.message(Uzb.uzb_text)
async def random_function_uzb(message: types.Message, state: FSMContext):
    await state.update_data(uzb_text = message.text)

    text = translator.translate(text=message.text, dest='uz')
    await message.answer(text.text,reply_markup=translate_button)
    await state.clear()
            


@dp.message(F.text == 'ru')
async def ru_function(message: types.Message, state: FSMContext):
    await state.set_state(Rus.rus_text)
    await message.answer('text kiriting')
    
@dp.message(Rus.rus_text)
async def random_function_rus(message: types.Message, state: FSMContext):
    text = translator.translate(text=message.text, dest='ru')
    await message.answer(text=text.text, reply_markup=translate_button)
    await state.clear()
            
            
  
            
            
            
            
@dp.message(F.text == 'en')
async def en_function(message: types.Message, state: FSMContext):
    await state.set_state(Eng.eng_text)
    await message.answer('text kiriting')
    
@dp.message(Eng.eng_text)
async def random_function_eng(message: types.Message, state: FSMContext):
    await state.update_data(eng_text = message.text)

    text = translator.translate(text=message.text, dest='en')
    await message.answer(text.text,reply_markup=translate_button)
    await state.clear()
            
    
    

async def main():
    await dp.start_polling(bot)
    
    
    
if __name__== '__main__':
    asyncio.run(main())