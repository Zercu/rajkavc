from aiogram import types
from aiogram.dispatcher import Dispatcher
from config import SUDO_USERS
from utils import get_stats

async def handle_stats(message: types.Message):
    if message.from_user.id not in SUDO_USERS:
        return
    total_groups, total_users = get_stats()
    await message.reply(f"Total Groups: {total_groups}\nTotal Users: {total_users}")

async def handle_adves(message: types.Message):
    if message.from_user.id not in SUDO_USERS:
        return
    ad_text = message.get_args()

def register_admin_handlers(dp: Dispatcher):
    dp.register_message_handler(handle_stats, commands="stats")
    dp.register_message_handler(handle_adves, commands="adves")
