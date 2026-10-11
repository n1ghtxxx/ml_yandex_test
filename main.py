import os
from dotenv import load_dotenv

def print_author():
    # Загружаем переменные окружения из файла .env
    load_dotenv()
    
    # Читаем значение переменной AUTHOR и присваиваем её переменной author
    author = os.getenv("AUTHOR")
    
    print(f"Автор проекта: {author}")

# Проверяем работу функции
if __name__ == "__main__":
    print_author()
