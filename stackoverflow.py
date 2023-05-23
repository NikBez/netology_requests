import requests
from datetime import datetime, timedelta
from pprint import pprint


class QuerySet:
    def __init__(self):
        self.questions = {}

    def get_last_questions(self, start_date, tag, order='asc'):
        params = {
            'fromdate': start_date,
            'order': order,
            'sort': 'creation',
            'tagged': tag,
            'site': 'stackoverflow',
        }
        response = requests.get('https://api.stackexchange.com/2.3/questions', params=params)
        response.raise_for_status()
        response = response.json()
        self.questions = response


if __name__ == '__main__':
    python_set = QuerySet()
    start_date = datetime.today() - timedelta(days=2)
    start_date = round(start_date.replace(hour=0, minute=0, second=0).timestamp())

    python_set.get_last_questions(start_date, 'python')

    pprint(python_set.questions)
