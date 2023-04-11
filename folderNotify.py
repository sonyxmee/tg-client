import configparser
from datetime import datetime

from telethon import TelegramClient, functions, types

config = configparser.ConfigParser()
config.read('config.ini')
api_id = int(config['TELEGRAM']['api_id'])
api_hash = config['TELEGRAM']['api_hash']
client = TelegramClient('account_telethon', api_id, api_hash)


async def main(folder_title):
    peers = []
    flag = False
    folders = await client(functions.messages.GetDialogFiltersRequest())

    for folder in folders[1:]:
        if folder.title == folder_title:
            flag = True
            try:
                # добавляю все каналы и чаты папки в список
                peers.extend(folder.pinned_peers)
                peers.extend(folder.include_peers)
                break
            except Exception:
                continue

    if not flag:
        print("Folder is not found.")
        return

    for peer in peers:
        await client(functions.account.UpdateNotifySettingsRequest(
            peer=peer,
            settings=types.InputPeerNotifySettings(
                silent=True,
                # mute_until=datetime(2023, 3, 16),  # mute for ... (для задания даты)
                mute_until=datetime(2037, 12, 31),  # mute forever
                # mute_until=datetime.max,  # данный вариант не работает,
                # скорее всего у телеграма в свойстве 'Mute forever' стоит дата до 2037 года, т.е. на 15 лет
            )
        ))
    print(f"Все уведомления чатов и каналов папки '{folder_title}' отключены")


if __name__ == '__main__':
    with client:
        folder_name = 'Учеба'
        client.loop.run_until_complete(main(folder_name))
