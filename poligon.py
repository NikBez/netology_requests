from environs import Env
import requests


env = Env()
env.read_env()


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        """Метод загружает файлы по списку file_list на яндекс диск"""

        url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        params = {
            'path': file_path,
            'overwrite': True
        }
        headers = {
            'Authorization': f'OAuth {self.token}',
            'Content-Type': 'application/json'
        }
        link_to_upload = requests.get(url, params=params, headers=headers)
        link_to_upload.raise_for_status()
        link_to_upload = link_to_upload.json()['href']

        response = requests.put(link_to_upload, data=open('to_upload/test.txt', 'rb'))
        if response.status_code == 201:
            print('Success')
        else:
            print(f'Error: {response.status_code}')


if __name__ == '__main__':

    token = env('YANDEX_POLIGON_TOKEN')
    file_path = 'From Netology/test.txt'

    uploader = YaUploader(token)
    uploader.upload(file_path)
