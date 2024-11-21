import requests
import json
import os
from dotenv import load_dotenv

# Завантаження змінних із .env
load_dotenv()

# Отримання змінних
API_URL = os.getenv('API_URL')
POSTS_FILE = os.getenv('POSTS_FILE')


def fetch_posts(api_url, output_file):
    """
    Завантажує дані з API і зберігає їх у файл JSON.

    :param api_url: URL API для отримання постів.
    :param output_file: Ім'я файлу для збереження даних.
    """
    try:
        # Виконання GET-запиту
        response = requests.get(api_url)

        # Перевірка статусу відповіді
        if response.status_code == 200:
            posts = response.json()  # Конвертація відповіді в JSON
            print(f"Отримано {len(posts)} постів.")

            # Запис даних у файл
            with open(output_file, 'w', encoding='utf-8') as file:
                json.dump(posts, file, indent=4, ensure_ascii=False)

            print(f"Дані збережено у файл {output_file}")
        else:
            print(f"Помилка при отриманні даних. Статус-код: {response.status_code}")
    except Exception as e:
        print(f"Сталася помилка: {e}")


# Використання функції
if __name__ == "__main__":
    fetch_posts(API_URL, POSTS_FILE)