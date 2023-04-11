import configparser
from telethon import TelegramClient

config = configparser.ConfigParser()
config.read('config.ini')
api_id = int(config['TELEGRAM']['api_id'])
api_hash = config['TELEGRAM']['api_hash']
client = TelegramClient('account_telethon', api_id, api_hash)

list_to_del = []


async def dry_run():
    print(f'The list of IDs for deleting chats: {list_to_del}')
    action = input('Would you like to delete these chats? (yes/no): ')
    while action not in ('yes', 'no'):
        print('Invalid response, enter again')
        action = input('Would you like to delete these chats? (yes/no): ')
    if action == 'yes':
        c = 0
        for el in list_to_del:
            await client.delete_dialog(el)
            c += 1
        print(f'{c} chats have been deleted')
    else:
        exit()


async def main():
    k = True
    async for dialog in client.iter_dialogs():
        try:
            if dialog.entity.deleted:
                list_to_del.append(dialog.entity.id)
                k = False
        except Exception:
            continue
    if k:
        print('Deleted accounts were not found.')
    else:
        await dry_run()


if __name__ == '__main__':
    with client:
        client.loop.run_until_complete(main())
