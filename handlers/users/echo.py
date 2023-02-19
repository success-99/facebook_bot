from aiogram import types

from loader import dp


# Echo bot
@dp.message_handler(state=None)
async def bot_echo(message: types.Message):
    await message.answer("Facebook havola kiritmadingiz!🤔🤔🤔\n"
                         "Yoki havolada xato bor!⚠️⚠️⚠️\n"
                         "Tekshirib qaytadan yuborinng")
