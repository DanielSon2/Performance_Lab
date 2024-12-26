import sys

def load_numbers(file_path):
    """Загружает числа из файла, обрабатывая ошибки."""
    try:
        with open(file_path, 'r') as f:
            return [int(line.strip()) for line in f]
    except FileNotFoundError:
        print(f"Не удалось найти файл: {file_path}")
        sys.exit(1)
    except ValueError:
        print("Ошибка в данных: файл должен содержать только целые числа.")
        sys.exit(1)

def calculate_median_moves(nums):
    """Вычисляет количество движений для выравнивания чисел к медиане."""
    nums.sort()  # Сортируем список чисел
    median = nums[len(nums) // 2]  # Определяем медиану
    return sum(abs(x - median) for x in nums)  # Суммируем разницу с медианой

def main():
    # Проверяем, передан ли путь к файлу через аргумент командной строки
    if len(sys.argv) != 2:
        print("python task4.py numbers.txt")
        sys.exit(1)

    file_path = sys.argv[1]  # Получаем путь к файлу из аргументов командной строки
    numbers = load_numbers(file_path)  # Загружаем числа из файла
    result = calculate_median_moves(numbers)  # Считаем минимальные движения
    print(result)  # Выводим результат

if __name__ == "__main__":
    main()
