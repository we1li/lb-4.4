def is_number(value):
    """Проверяет, является ли введённое значение числом."""
    try:
        float(value)  # Пытаемся преобразовать в число
        return True
    except ValueError:
        return False

def main():
    # Запрос двух значений от пользователя
    value1 = input("Введите первое значение: ")
    value2 = input("Введите второе значение: ")

    # Проверяем, являются ли оба значения числами
    if is_number(value1) and is_number(value2):
        # Если оба числа, выводим их сумму
        result = float(value1) + float(value2)
        print(f"Сумма чисел: {result}")
    else:
        # Если хотя бы одно значение не является числом, выполняем конкатенацию строк
        result = value1 + value2
        print(f"Конкатенация строк: {result}")

if __name__ == "__main__":
    main()
