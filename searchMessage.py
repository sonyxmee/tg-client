import configparser
from datetime import datetime
from telethon import TelegramClient, functions, types

config = configparser.ConfigParser()
config.read('config.ini')
api_id = int(config['TELEGRAM']['api_id'])
api_hash = config['TELEGRAM']['api_hash']
client = TelegramClient('account', api_id, api_hash)


async def main(search_req, folder):
    count = 0
    peers = []
    folders = await client(functions.messages.GetDialogFiltersRequest())

    for folder in folders[1:]:
        if folder.title == folder:
            try:
                # добавляю все каналы и чаты папки в список
                peers.extend(folder.pinned_peers)
                peers.extend(folder.include_peers)
                peers.extend(folder.exclude_peers)
                break
            except Exception:
                continue
    for peer in peers:
        result = await client(functions.messages.SearchRequest(
            peer=peer,
            q=search_req,
            filter=types.InputMessagesFilterEmpty(),
            min_date=datetime(2013, 8, 14),
            max_date=datetime.now(),
            offset_id=0,
            add_offset=0,
            limit=10,
            max_id=0,
            min_id=0,
            hash=-12398745604826,
        ))
        # print(result.stringify())
        count += len(result.messages)

        for mes in result.messages:
            dialog_id = 0
            from_id = 0

            match type(mes.peer_id):
                case types.PeerChannel:
                    dialog_id = mes.peer_id.channel_id
                    from_id = mes.from_id.user_id
                case types.PeerUser:
                    dialog_id = mes.peer_id.user_id
                    from_id = dialog_id
                case types.PeerChat:
                    dialog_id = mes.peer_id.chat_id
                    from_id = mes.from_id.user_id

            print(f'Dialog id: {dialog_id}\nSender id: {from_id}\n'
                  f'Message: {mes.message}\n\n')

    print(f'Count of founded messages: {count}\n\n')


if __name__ == '__main__':
    with client:
        search_request = 'Привет'
        folder_name = 'Учеба'
        client.loop.run_until_complete(main(search_request, folder_name))
