import configparser
from telethon import TelegramClient

config = configparser.ConfigParser()
config.read('config.ini')
api_id = int(config['TELEGRAM']['api_id'])
api_hash = config['TELEGRAM']['api_hash']
client = TelegramClient('account', api_id, api_hash)


async def main():
    k = True
    async for dialog in client.iter_dialogs():
        try:
            if dialog.entity.deleted:
                print(f'The ID of the deleted account: {dialog.entity.id}')
                k = False
                await client.delete_dialog(dialog)
        except Exception:
            continue
    if k:
        print('Deleted accounts were not found.')


with client:
    client.loop.run_until_complete(main())
