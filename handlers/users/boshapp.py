from aiogram import types
from loader import dp,bot
from aiogram.dispatcher.filters import Text
from facebook import facebook

@dp.message_handler(commands='boshla')
async def boshla(message:types.Message):
    await message.answer('Facebook havolasini tashlang')


# @dp.message_handler()
# async def cmd_answer(message: types.Message):
#     if message.text.startswith('https://fb') \
#             or message.text.startswith('https://www.facebook.com'):
@dp.message_handler(Text(startswith="https://", ))
async def send_link(message: types.Message):
        link = message.text
        data5 = facebook(link)
        if data5 == "bed":
            await message.answer("Hechnarsa topilmadi 😔")
        else:
            await message.delete()
            xabar = await bot.send_message(chat_id=message.chat.id, text="kuting")
            for i in range(1, 11):
                text0 = i * 10
                text1 = i * "▪️"
                text2 = (10 - i) * "▫️️"
                await xabar.edit_text(f"{text0}%\n{text1}{text2}")
            await xabar.delete()
            await message.answer_video(data5)

