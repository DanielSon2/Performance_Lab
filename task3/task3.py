import json
import sys # для возможности запуска программы через терминал (получения аргументов командной строки)

# Функция для чтения JSON-файла
def read_json(filepath):
    try:
        with open(filepath, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Ошибка: Файл '{filepath}' не найден.")
        sys.exit(1)
    except json.JSONDecodeError:
        print(f"Ошибка: Неверный формат JSON в файле '{filepath}'.")
        sys.exit(1)

# Рекурсивная функция для замены значений и очистки пустых полей
def update_values(test_list, value_map):
    for test in test_list:
        # Проверяем и заменяем значение по ID, если оно существует в value_map
        value = value_map.get(test['id'], "")
        if value:
            test['value'] = value
        elif 'value' in test:
            del test['value']  # Удаляем пустое поле 'value'

        # Если есть вложенные значения (values), продолжаем рекурсивную обработку
        if 'values' in test:
            update_values(test['values'], value_map)
            
            # Убираем поле 'values', если оно пустое после обработки
            if not test['values']:
                del test['values']

# Функция для генерации итогового отчета
def generate_report(tests_data, values_data, output_filepath):
    # Преобразуем список значений в словарь для быстрого поиска
    value_map = {item['id']: item['value'] for item in values_data}
    
    # Обновляем тестовые данные значениями и удаляем ненужные поля
    update_values(tests_data['tests'], value_map)
    
    # Сохраняем результат в файл
    with open(output_filepath, 'w') as output_file:
        json.dump(tests_data, output_file, indent=4)

def main():
    # Проверяем количество переданных аргументов
    if len(sys.argv) != 4:
        print("python task3.py values.json tests.json report.json")
        sys.exit(1)

    # Получаем пути к файлам из аргументов командной строки
    values_filepath = sys.argv[1]
    tests_filepath = sys.argv[2]
    output_filepath = sys.argv[3]

    # Загружаем данные из JSON-файлов
    values_data = read_json(values_filepath)
    tests_data = read_json(tests_filepath)

    # Проверяем наличие нужных данных в загруженных файлах
    if 'values' not in values_data or 'tests' not in tests_data:
        print("Ошибка: Неправильная структура файлов.")
        sys.exit(1)

    # Создаем итоговый отчет
    generate_report(tests_data, values_data['values'], output_filepath)
    print(f"Отчет успешно сохранен в '{output_filepath}'.")

if __name__ == "__main__":
    main()
