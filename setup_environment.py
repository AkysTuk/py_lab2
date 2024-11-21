import os
import subprocess
import sys

def install_dependencies():
    """
    Встановлює залежності з requirements.txt.
    """
    try:
        # Перевіряємо, чи існує файл requirements.txt
        if not os.path.exists("requirements.txt"):
            print("Файл requirements.txt не знайдено.")
            return

        # Використовуємо pip для встановлення бібліотек
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("Усі залежності успішно встановлено.")
    except Exception as e:
        print(f"Сталася помилка при встановленні залежностей: {e}")

if __name__ == "__main__":
    install_dependencies()