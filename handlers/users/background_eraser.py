from io import BytesIO
from PIL import Image
from rembg import remove
from aiogram.types import Message
from keyboards.inline.color_button import keyboard, bg_colors
from aiogram.dispatcher.filters import Command
from aiogram.dispatcher import FSMContext
from aiogram import types
from loader import dp

@dp.message_handler(Command("start"), state=None)
@dp.message_handler(content_types=types.ContentType.PHOTO, state=None)
async def cmd_start(message: Message, state: FSMContext):
    if not message.photo:
        await message.reply('Iltimas, suwret jibeseniz..')
        return
    await state.update_data(photo=message.photo)
    await message.reply("Suwrettin artqi renin tanlan!", reply_markup=keyboard)

@dp.callback_query_handler(lambda c: c.data in bg_colors.keys())
async def process_callback_button_color(callback_query: types.CallbackQuery, state: FSMContext):
    color = callback_query.data
    message = callback_query.message
    photo = (await state.get_data())['photo'][-1] if (await state.get_data()).get('photo') else None

    if photo is None:
        await message.answer("Islew ushin foto joq!")
        return

    photo_bytes = BytesIO()
    await photo.download(photo_bytes)
    photo_bytes.seek(0)
    output = remove(photo_bytes.getvalue())
    no_bg_img_bytes = BytesIO(output) # type: ignore

    with Image.open(no_bg_img_bytes) as im:
        bg = bg_colors[color]
        new_im = Image.new("RGBA", im.size, bg)
        new_im.paste(im, mask=im)
        new_im_bytes = BytesIO()
        new_im.save(new_im_bytes, format="PNG")
        new_im_bytes.seek(0)

    await callback_query.message.bot.send_photo(callback_query.message.chat.id, new_im_bytes)
    await callback_query.answer()
    await state.finish()