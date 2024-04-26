from aiogram import F, types, Router
from aiogram.filters import CommandStart, Command
from aiohttp import ClientSession
from common.keyboard import main_kb

user_private_router = Router()


@user_private_router.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer(f"Hi {message.from_user.first_name} \n insert your WB token", reply_markup=main_kb)

@user_private_router.message(Command("help"))
async def help(message: types.Message):
    print(message)
    await message.reply("how can I help you ?")


@user_private_router.message()
async def handle_token(message: types.Message):
    token = message.text
    await message.answer("Thank you! Now I will make a request with your token.")
    
    async with ClientSession() as session:
        headers = {'Authorization': f'Bearer {token}'}
        async with session.post('https://statistics-api.wildberries.ru/api/v1/supplier/incomes', headers=headers) as resp:
            response_text = await resp.text()
            await message.answer(f"API response: {response_text}")
    
    
@user_private_router.message()
async def echo_to_user(message: types.Message):
    await message.answer(message.text)