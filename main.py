import json

import requests
from fake_useragent import UserAgent

ua = UserAgent(verify_ssl=False)

URL = 'https://........../wp-json/wp/v2/posts?per_page=100&page=1'
FILE_NAME = '...........json'


def main():
    headers = {
        'accept': '*/*',
        'user-agent': ua.random
    }

    count_post = int(requests.get(url=URL).headers['X-WP-TotalPages'])

    with open(FILE_NAME, "w", encoding="utf-8") as file:
        file.write("[")
        for page in range(1, count_post):
            LINK = f'https://........../wp-json/wp/v2/posts?per_page=100&page={page}'
            response = requests.get(url=LINK, headers=headers)
            print(f'[*] Being processed: {LINK}')
            data = response.json()
            content = {}
            for i in data:
                content['id'] = i.get('id')
                content['title'] = i.get('title')['rendered']
                content['date'] = i.get('date')
                content['link'] = i.get('link')
                content['content'] = i.get('content')['rendered']

                json.dump(content, file, indent=4, ensure_ascii=False)
                file.write(',\n')
        file.write(']')


if __name__ == '__main__':
    main()
