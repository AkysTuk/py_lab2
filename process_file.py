import os
from dotenv import load_dotenv

# Завантаження змінних із .env
load_dotenv()

# Отримання змінних
INPUT_FILE = os.getenv('INPUT_FILE')
OUTPUT_FILE = os.getenv('OUTPUT_FILE')


def process_file(input_filename, output_filename):
    """
    Обробляє текстовий файл:
    - Рахує кількість рядків.
    - Рахує кількість слів у кожному рядку.
    - Записує результати у новий файл.
    """
    try:
        # Відкриваємо файл для читання
        with open(input_filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        # Рахуємо кількість рядків
        line_count = len(lines)
        print(f"Кількість рядків у файлі: {line_count}")

        # Обробляємо кожен рядок
        results = []
        for i, line in enumerate(lines, 1):
            word_count = len(line.split())  # Рахуємо кількість слів у рядку
            result = f"Рядок {i}: {line.strip()} (Слів: {word_count})"
            results.append(result)
            print(result)

        # Записуємо результати у файл
        with open(output_filename, 'w', encoding='utf-8') as output_file:
            output_file.write(f"Кількість рядків: {line_count}\n")
            output_file.write("\n".join(results))

        print(f"Дані збережено у файл {output_filename}")

    except FileNotFoundError:
        print(f"Файл {input_filename} не знайдено.")
    except Exception as e:
        print(f"Сталася помилка: {e}")


# Використання
if __name__ == "__main__":
    process_file(INPUT_FILE, OUTPUT_FILE)