from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

bg_colors = {
    "blue": (0, 0, 255),
    "red": (255, 0, 0),
    "green": (0, 255, 0),
    "yellow": (255, 255, 0),
    "gray": (128, 128, 128),
    "pink": (255, 96, 208),
    "light blue": (80, 208, 255),
    "orange": (255, 160, 16),
    "brown": (160, 128, 96),
}

keyboard = InlineKeyboardMarkup()
for color in bg_colors.keys():
    button = InlineKeyboardButton(text=color, callback_data=color)
    keyboard.add(button)