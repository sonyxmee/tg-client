import asyncio
import configparser

from pyrogram import Client
from pyrogram.raw import functions

config = configparser.ConfigParser()
config.read('config.ini')
api_id = config['TELEGRAM']['api_id']
api_hash = config['TELEGRAM']['api_hash']


async def main():
    max_common_chat = 0
    max_users = []
    async with Client('account_test', api_id, api_hash) as app:
        async for dialog in app.get_dialogs():
            try:
                common = await app.get_common_chats(dialog.chat.id)
                count_common = len(common)
                if count_common > max_common_chat:
                    max_users = [{dialog.chat.id: dialog.chat.title or dialog.chat.username}]
                    max_common_chat = count_common
                elif count_common == max_common_chat:
                    max_users.append({dialog.chat.id: dialog.chat.title or dialog.chat.username})
            except ValueError as e:
                continue
    print(f"Максимальное количество общих чатов: {max_common_chat}")
    print(f"Информация о пользователях с макс. кол-м общих чатов (user_id: user_first_name): \n"
          f"{max_users}")


if __name__ == '__main__':
    asyncio.run(main())
