#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import argparse
import logging
from pathlib import Path

# Настройка логгирования
logging.basicConfig(
    filename='routes.log',  # Имя файла для записи логов
    level=logging.INFO,      # Уровень логирования (INFO - для общего учета событий)
    format='%(asctime)s - %(levelname)s - %(message)s'  # Формат логов
)

# Создаем путь к файлу данных в домашнем каталоге пользователя
file_path = Path("G:/ООП/4.4/idz1") / "idz.json"

# Функция для ввода данных о маршрутах
def add_route(routes, start, end, number):
    """Добавляет новый маршрут в список маршрутов."""
    
    # Проверка на дубликаты маршрута по номеру
    for route in routes:
        if route["number"] == number:
            logging.warning(f"Попытка добавить дублирующий маршрут: {number}.")
            print(f"Ошибка: Маршрут с номером {number} уже существует.")
            return routes  # Возвращаем неизменённый список маршрутов
    
    # Создаем словарь для нового маршрута
    route = {
        "start": start,
        "end": end,
        "number": number
    }
    routes.append(route)  # Добавляем маршрут в список
    logging.info(f"Добавлен маршрут: {route}")  # Логируем добавление маршрута
    return routes

# Функция для вывода информации о маршруте по номеру
def find_route(routes, number):
    """Ищет маршрут по его номеру и выводит его информацию."""
    
    found = False  # Флаг, указывающий на то, найден ли маршрут
    for route in routes:
        if route["number"] == number:  # Сравниваем номер маршрута
            print("Начальный пункт маршрута:", route["start"])
            print("Конечный пункт маршрута:", route["end"])
            found = True  # Устанавливаем флаг в True, если маршрут найден
            break  # Прекращаем поиск, так как маршрут найден
    if not found:
        logging.warning(f"Маршрут с номером {number} не найден.")  # Логируем предупреждение
        print("Маршрут с таким номером не найден.")

def display_menu():
    """Выводит меню доступных команд."""
    print("Доступные команды:")
    print("add - Добавить новый маршрут")  # Команда для добавления маршрута
    print("find - Найти маршрут по номеру")  # Команда для поиска маршрута
    print("exit - Выйти из программы")  # Команда для выхода

if __name__ == '__main__':
    # Попробуем загрузить маршруты из файла
    try:
        with open(file_path, "r", encoding='utf-8') as file:
            routes = json.load(file)  # Загружаем маршруты из файла
    except FileNotFoundError:
        logging.info("Файл не найден, создается новый.")  # Логируем, что файл не найден
        routes = []  # Инициализируем пустой список маршрутов
    except json.JSONDecodeError:
        logging.error("Ошибка чтения файла. Проверьте формат JSON.")  # Логируем ошибку
        print("Ошибка чтения файла. Проверьте формат JSON.")
        routes = []  # Инициализируем пустой список маршрутов

    while True:
        display_menu()  # Отображаем меню
        command = input("Введите команду: ").strip().lower()  # Получаем команду от пользователя

        if command == "exit":  # Если команда "exit", выходим из программы
            print("Выход из программы.")
            break
        elif command == "add":  # Если команда "add", добавляем новый маршрут
            start = input("Введите начальный пункт маршрута: ")  # Получаем начальный пункт
            end = input("Введите конечный пункт маршрута: ")  # Получаем конечный пункт
            number = input("Введите номер маршрута: ")  # Получаем номер маршрута
            routes = add_route(routes, start, end, number)  # Добавляем маршрут
        elif command == "find":  # Если команда "find", ищем маршрут по номеру
            number = input("Введите номер маршрута для поиска: ")  # Получаем номер маршрута
            find_route(routes, number)  # Ищем маршрут
        else:
            print("Неизвестная команда. Попробуйте снова.")  # Если команда не распознана

        # Сохраняем данные в файл JSON после ввода информации
        try:
            with open(file_path, "w", encoding='utf-8') as file:
                json.dump(routes, file, ensure_ascii=False, indent=4)  # Сохраняем маршруты в файл
                logging.info("Данные успешно сохранены в файл.")  # Логируем успешное сохранение
        except Exception as e:
            logging.error(f"Ошибка при сохранении данных в файл: {e}")  # Логируем ошибку
            print(f"Ошибка при сохранении данных в файл: {e}")
