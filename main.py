import requests
from typing import Final

API_KEY: Final[str] = '818a003d8a0054f54908f3fe0c976f8c923ee' 
BASE_URL: Final[str] = 'https://cutt.ly/api/api.php'


def shorten(full_link: str):
    payload: dict = {'key': API_KEY, 'short':full_link }
    request = requests.get(BASE_URL, params=payload)
    data: dict = request.json()

    if url_data := data.get('url'):
        if url_data['status'] == 7:
            short_link: str = url_data['shortLink']
            print('Link:', short_link)
        else:
            print('Error status:', url_data['status'])


def main():
    # Take user input
    link: str = input('Enter a link: ')

    # Shorten the link
    shorten(link)


if __name__ == '__main__':
    main()
