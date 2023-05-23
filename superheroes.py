import requests
from urllib.parse import urljoin


BASE_PATH = 'https://akabab.github.io/superhero-api/api/'
ROUTES = {
    'ALL': 'all.json'
}


def find_smartest_hero(targets):

    response_all = requests.get(urljoin(BASE_PATH, ROUTES['ALL']))
    response_all.raise_for_status()
    intelligence_max = 0
    smartest = ''
    for hero in response_all.json():
        if hero['name'] in targets and hero['powerstats']['intelligence'] > intelligence_max:
            smartest = hero['name']
    return smartest


if __name__ == '__main__':
    hero = find_smartest_hero(['Hulk', 'Captain America', 'Thanos'])
    print(hero)

