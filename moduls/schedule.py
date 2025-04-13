
import asyncio
from datetime import datetime

from personal_information import TOKEN
from json_file import is_authorized, load_schedule, save_schedule
from inline import keyboard

from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from aiogram_calendar import SimpleCalendar, SimpleCalendarCallback


bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message(Command("set"))
async def cmd_set(message: Message):
    if not is_authorized(message):
        await message.answer("Цей бот лише для особистого використання.")
        return
    await message.answer("Вибери дату з календаря:", reply_markup=await SimpleCalendar().start_calendar())
    

@dp.callback_query(SimpleCalendarCallback.filter())
async def process_calendar(callback_query: CallbackQuery, callback_data: SimpleCalendarCallback):
    selected_date = callback_data
    global DAY
    DAY = str(selected_date.day) +"."+ str(selected_date.month)+"."+ str(selected_date.year)
    global weekday
    weekday = datetime.strptime(DAY, "%d.%m.%Y").weekday()
    await callback_query.message.answer(f"Обрана дата: {selected_date.day}.{selected_date.month}.{selected_date.year} Обери опцію.", reply_markup=keyboard)
    await callback_query.message.delete()
    await callback_query.answer()

@dp.callback_query(F.data == "minibar")
async def minibar(callback_query: CallbackQuery):
    schedule = load_schedule()
    if weekday == 0 or weekday == 3 or weekday == 5:       
        schedule[DAY] = {"06:00": "wake_up",
                        "09:00": "work",
                        "18:30": "workout",
                        "21:00": "relax",
                        "23:59": "sleep"}
    else:
        schedule[DAY] = {"06:00": "wake_up",
                        "09:00": "work",
                        "19:00": "relax",
                        "23:59": "sleep"}        
    save_schedule(schedule)
    await callback_query.message.delete()
    await callback_query.answer("Зміна збережена")


@dp.callback_query(F.data == "club")
async def calb(callback_query: CallbackQuery):
    schedule = load_schedule()
    if weekday == 0 or weekday == 3 or weekday == 5:          
        schedule[DAY] = {"06:00": "wake_up",
                        "08:00": "workout",
                        "11:00": "work",
                        "22:00": "relax",
                        "23:59": "sleep"}
    else:
        schedule[DAY] = {"08:00": "wake_up",
                        "11:00": "work",
                        "22:00": "relax",
                        "23:59": "sleep"}
    save_schedule(schedule)
    await callback_query.message.delete()
    await callback_query.answer("Зміна збережена")

    
@dp.callback_query(F.data == "olivera")
async def olivera(callback_query: CallbackQuery):
    schedule = load_schedule()
    if weekday == 0 or weekday == 3 or weekday == 5:          
        schedule[DAY] = {"04:30": "wake_up",
                        "06:30": "work",
                        "16:30": "workout",
                        "19:00": "relax",
                        "22:00": "sleep"}
    else:
        schedule[DAY] = {"04:30": "wake_up",
                        "06:30": "work",
                        "16:30": "relax",
                        "22:00": "sleep"}
    save_schedule(schedule)
    await callback_query.message.delete()
    await callback_query.answer("Зміна збережена")


@dp.callback_query(F.data == "weekend")
async def weekend(callback_query: CallbackQuery):
    schedule = load_schedule()
    if weekday == 0 or weekday == 3 or weekday == 5:   
        schedule[DAY] = {"08:00": "wake_up",
                        "10:00": "workout",
                        "13:00": "relax",
                        "23:59": "sleep"}
    else:
        schedule[DAY] = {"08:00": "wake_up",
                        "10:00": "relax",
                        "23:59": "sleep"}
    save_schedule(schedule)
    await callback_query.message.delete()
    await callback_query.answer("Зміна збережена")

@dp.callback_query(F.data == "college")
async def college(callback_query: CallbackQuery):
    schedule = load_schedule()
    if weekday == 0 or weekday == 3 or weekday == 5:    
        schedule[DAY] = {"07:00": "wake_up",
                        "09:00": "study",
                        "16:00": "workout",
                        "18:00": "relax",
                        "23:59": "sleep"}
    else:
        schedule[DAY] = {"07:00": "wake_up",
                        "09:00": "study",
                        "16:00": "relax",
                        "23:59": "sleep"}
    save_schedule(schedule)
    await callback_query.message.delete()
    await callback_query.answer("Зміна збережена")



async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
