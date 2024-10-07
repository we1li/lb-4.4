import random

def get_int_input(prompt):
    """Запрашивает у пользователя целое число и проверяет правильность ввода."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Ошибка: Введите целое число.")

def generate_matrix(rows, cols, start, end):
    """Генерирует матрицу случайных чисел с указанными параметрами."""
    matrix = []
    for _ in range(rows):
        row = [random.randint(start, end) for _ in range(cols)]
        matrix.append(row)
    return matrix

def print_matrix(matrix):
    """Выводит матрицу на экран."""
    for row in matrix:
        print(" ".join(map(str, row)))

def main():
    # Запрашиваем параметры у пользователя
    rows = get_int_input("Введите количество строк: ")
    cols = get_int_input("Введите количество столбцов: ")
    start = get_int_input("Введите минимальное значение диапазона: ")
    end = get_int_input("Введите максимальное значение диапазона: ")

    if start > end:
        print("Ошибка: минимальное значение диапазона не может быть больше максимального.")
        return

    # Генерация и вывод матрицы
    matrix = generate_matrix(rows, cols, start, end)
    print("Сгенерированная матрица:")
    print_matrix(matrix)

if __name__ == "__main__":
    main()
