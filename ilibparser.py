from requests import get
from sys      import argv
from bs4      import BeautifulSoup
from os       import startfile

chapters = []

addr = argv[1]

while True:
    print(f'Глава {addr.split(".")[-2].split("/")[0]}:\n\tПолучение текста.. ', end='')
    soup = BeautifulSoup(get(addr).text, 'html.parser')

    lines = soup.find_all('div', {'id': 'text'})
    for line in lines:
        chapters.append(line.get_text().split('\n')[2:-1])
    print('ОК')

    print('\tПоиск ссылки на следующую главу.. ', end='')
    navlinks = soup.find_all('a', {'class': 'navlink'})
    if len(navlinks) != 2:
        print('Не найдена\n')
        break
    print('Найдена\n')
    
    addr = f'https://ilibrary.ru{navlinks[1].get("href")}'

print('\tПолучение заголовка.. ', end='')
title = soup.title.string.split('. ')[-3]
print('Готово\n')

print('Получение завершено\n\nВыберите формат выходного файла (введите число):\n\t[1] HTML\n\t[2] Plain Text (.txt)\n')

formats = {
    '1': 'html',
    '2': 'text'
}
inp = None

while inp not in formats:
    inp = input('> ')

match formats[inp]:
    case 'html':

        print('\nПодготовка текста.. ', end='')
        for i in range(len(chapters)):
            for j in range(len(chapters[i])):
                chapters[i][j] = '<p>' + chapters[i][j] + '</p>'
            chapters[i] = '\n'.join(chapters[i])
        out = '''<!doctype html>
<html>
<head>
    <title>''' + title + '''</title>
</head>
<body>
    <style>
        * {
            margin: 0;
            padding: 0
        }

        body {
            padding: 10pt;
            font-size: 25pt
        }

        button {
            padding: 5pt;
            text-align: "center";
        }

        p {
            margin-bottom: 10pt;
        }
    </style>
    <script>
        dark = false;

        function switch_theme() {
            dark = !dark;
            if (dark) {
                document.body.style.backgroundColor = 'rgb(51, 51, 51)';
                document.body.style.color = 'rgb(255, 255, 255)';
            } else {
                document.body.style.backgroundColor = 'rgb(255, 255, 255)';
                document.body.style.color = 'rgb(0, 0, 0)';
            }
        }
    </script>
    <button onclick="switch_theme()">Сменить тему</button>'''
        out += '<br><br>'.join(chapters)
        out += '''</body>
</html>'''
        print('Готово\nСохранение.. ', end='')
        with open(f'{title}.html', 'w') as file:
            file.write(out)
        print('Готово\n')
        startfile(f'{title}.html')

    case 'text':
        print('\nПодготовка текста.. ', end='')
        for i in range(len(chapters)):
            chapters[i] = '\n'.join(chapters[i])
        out = '\n\n'.join(chapters)
        print('Готово\nСохранение.. ', end='')
        with open(f'{title}.txt', 'w') as file:
            file.write(out)
        print('Готово\n')
        startfile(f'{title}.txt')
