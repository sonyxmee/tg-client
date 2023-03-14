deleteChats.py - программа для удаления всех чатов с удалёнными аккаунтами.

Алгоритм программы:
1) получить список всех чатов
2) у чата получить User
3) проверить если у User поле deleted: true, то удалить чат

Чтобы запустить программу:
1) pip install -r requirements.txt
2) создать приложение [здесь](https://my.telegram.org/) 
3) получить api_id, api_hash и вставить эти знаечния в config.ini
4) запустить файл deleteChat.py

Используется библиотека Telethon


commonChats.py - программа для получения списка людей, с которыми у пользователя больше всего общих групп в Telegram.

Алгоритм программы:
1) получить список всех контактов
2) найти наибольшее кол-во общих чатов среди всех контактов
3) создать список пользователей, с которыми больше всего общих групп

Чтобы запустить программу:
1) pip install -r requirements.txt
2) создать приложение [здесь](https://my.telegram.org/) 
3) получить api_id, api_hash и вставить эти знаечния в config.ini
4) запустить файл commonChats.py

Используется библиотека Pyrogram

