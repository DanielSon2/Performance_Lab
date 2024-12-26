import sys # для возможности запуска программы через терминал (получения аргументов командной строки)

# Функция для получения данных о круге из файла
def read_circle_data(file_path):
    with open(file_path, 'r') as file:
        # Считываем координаты центра и радиус окружности
        center_x, center_y = map(float, file.readline().split())
        radius = float(file.readline())
    return (center_x, center_y, radius)

# Функция для получения данных о точках из файла
def read_points(file_path):
    points = []
    with open(file_path, 'r') as file:
        # Считываем координаты точек
        for line in file:
            points.append(tuple(map(float, line.split())))
    return points

# Функция для определения положения точки относительно окружности
def check_point_position(circle_data, point_data):
    cx, cy, r = circle_data
    px, py = point_data
    distance_squared = (px - cx) ** 2 + (py - cy) ** 2  # Расстояние от точки до центра окружности в квадрате
    radius_squared = r ** 2  # Радиус окружности в квадрате

    if distance_squared == radius_squared:
        return 0  # Точка на окружности
    elif distance_squared < radius_squared:
        return 1  # Точка внутри окружности
    else:
        return 2  # Точка вне окружности

# Основная функция программы
def main():
    if len(sys.argv) != 3:
        print("python task2.py circle.txt points.txt")
        sys.exit(1)

    circle_file = sys.argv[1]
    points_file = sys.argv[2]

    # Чтение данных окружности и точек
    circle_data = read_circle_data(circle_file)
    points = read_points(points_file)

    # Для каждой точки вычисляем её положение относительно окружности
    for point in points:
        print(check_point_position(circle_data, point))

# Запуск основной функции, если скрипт запускается напрямую
if __name__ == "__main__":
    main()