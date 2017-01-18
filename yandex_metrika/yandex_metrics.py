from urllib.parse import urlencode, urlparse, urljoin
from pprint import pprint
import requests

AUTHORIZE_URL = 'https://oauth.yandex.ru/authorize'
APP_ID = '48b6b00f8a11492ea37d7ea0f7637eb3'

auth_data = {
    'response_type': 'token',
    'client_id': APP_ID
}
print('?'.join((AUTHORIZE_URL, urlencode(auth_data))))

TOKEN = 'AQAAAAASwZgUAAP4G4E91-sJuUsWupHwZLwyFgU'


class YandexMetrika(object):
    _METRIKA_STAT_URL = 'https://api-metrika.yandex.ru/stat/v1/'
    _METRIKA_MANAGEMENT_URL = 'https://api-metrika.yandex.ru/management/v1/'
    token = None

    def __init__(self, token):
        self.token = token

    def get_header(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def counter_list(self):
        url = urljoin(self._METRIKA_MANAGEMENT_URL, 'counters')
        response = requests.get(url, headers=self.get_header())
        counter_list = [c['id'] for c in response.json()['counters']]
        return counter_list

    def get_visits_count(self, counter_id):
        url = urljoin(self._METRIKA_STAT_URL, 'data')
        params = {
            'id': counter_id,
            'metrics': 'ym:s:visits'
        }
        response = requests.get(url, params, headers=self.get_header())
        pprint(response.json())
        visits_count = response.json()['data'][0]['metrics'][0]
        return visits_count


metrika = YandexMetrika(TOKEN)
print(YandexMetrika.__dict__)
print(metrika.__dict__)

for counter in metrika.counter_list():
    print(metrika.get_visits_count(counter))
