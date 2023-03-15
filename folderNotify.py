import configparser
from datetime import datetime

from telethon import TelegramClient, functions, types

config = configparser.ConfigParser()
config.read('config.ini')
api_id = int(config['TELEGRAM']['api_id'])
api_hash = config['TELEGRAM']['api_hash']
client = TelegramClient('account', api_id, api_hash)


async def main():
    peers = []
    folders = await client(functions.messages.GetDialogFiltersRequest())

    folder_name = 'Учеба'
    for folder in folders[1:]:
        if folder.title == folder_name:
            try:
                # добавляю все каналы и чаты папки в список
                peers.extend(folder.pinned_peers)
                peers.extend(folder.include_peers)
                peers.extend(folder.exclude_peers)
                break
            except Exception:
                continue
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
    print(f'Уведомления у всех пользователей чата {folder_name} отключены')


with client:
    client.loop.run_until_complete(main())
