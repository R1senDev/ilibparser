# ilibparser

Немного умный парсер книг для сайта ilibrary.ru. Проверен на Windows 11.

## Причина архивации репозитория: он говно

# Как пользоваться?

1. Откройте командную строку/PowerShell/Терминал в папке со скриптом.
2. Если вы запускаете парсер первый раз, выполните команду `pip install -r requirements.txt`.
3. Передите на страницу одной из глав произведения, которое хотите спарсить. **Обратите внимание:** в результате будут получены только указанная глава и все последующие. Так, если вы укажете ссылку на четвёртую главу, первые три будут проигнорированы.
4. Скопируйте ссылку на страницу.
5. Запустите скрипт `ilibparser.py`, вставив скопированную ссылку на место первого аргумента запуска. Напимер, так:
``` bash
python ilibparser.py https://ilibrary.ru/text/1180/p.1/index.html/index.html
```
6. Дождитесь окончания процесса парсинга и выберите подходящий формат: HTML, если хотите читать через браузер или TXT, если вам по душе текстовые редакторы.
7. После сохранения файла он откроется автоматически. Для повторного открытия парсить всё сначала не нужно: файлы остаются в папке, из которой был запущен скрипт.
