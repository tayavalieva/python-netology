import requests

KEY = 'trnsl.1.1.20170107T093148Z.c5d7c74b2aaacd99.313ded75f925af251c5cd2848a71b2c82c3005b0'
URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'


def read_text_from_file(input_path):
    with open(input_path) as input_file:
        return input_file.read()


def translate(input_path, output_path, input_lang, output_lang='ru'):
    """
        YANDEX translation plugin

        docs: https://tech.yandex.ru/translate/doc/dg/reference/translate-docpage/

        https://translate.yandex.net/api/v1.5/tr.json/translate ?
        key=<API-ключ>
         & text=<переводимый текст>
         & lang=<направление перевода>
         & [format=<формат текста>]
         & [options=<опции перевода>]
         & [callback=<имя callback-функции>]

        :param text: <str> text for translation.
        :return: <str> translated text.
        """
    input_text = read_text_from_file(input_path)
    params = {
        'key': KEY,
        'text': input_text,
        'lang': input_lang + '-' + output_lang,
    }
    response = requests.get(URL, params=params).json()
    with open(output_path, 'w', encoding='UTF8') as output_file:
        output_text = ''.join(response.get('text', []))
        output_file.write(output_text)
    print('Перевели и сохранили в указанный файл.')


translate('C:\\Users\\Taya\\Desktop\\Coursera analytics\\Python\\python-netology\\yandex_translator\\DE.txt',
          'C:\\Users\\Taya\\Desktop\\Coursera analytics\\Python\\python-netology\\yandex_translator\\DE_RU.txt', 'de')
