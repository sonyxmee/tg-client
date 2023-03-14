import asyncio
import configparser

from pyrogram import Client

config = configparser.ConfigParser()
config.read('config.ini')
api_id = config['TELEGRAM']['api_id']
api_hash = config['TELEGRAM']['api_hash']


async def main():
    max_common_chat = 0
    max_users = []
    async with Client('account_', api_id, api_hash) as app:
        contacts = await app.get_contacts()
        for contact in contacts:
            common = await app.get_common_chats(contact.id)
            count_common = len(common)
            if count_common > max_common_chat:
                max_users = [{contact.id: contact.first_name or contact.username}]
                max_common_chat = count_common
            elif count_common == max_common_chat:
                max_users.append({contact.id: contact.first_name or contact.username})

    print(f"Максимальное количество общих чатов: {max_common_chat}")
    print(f"Информация о пользователях с макс. кол-м общих чатов (user_id: user_first_name): \n"
          f"{max_users}")


asyncio.run(main())
