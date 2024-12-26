import sys # для возможности запуска программы через терминал (получения аргументов командной строки)

def circular_array(n: int, m: int):
    path = []
    current_value = 1
    while True:
        path.append(str(current_value))
        current_value = 1 + (current_value + m - 2) % n
        if current_value == 1:
            break

    print(''.join(path))


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("python task1.py 4 3")
    else:
        try:
            n = int(sys.argv[1])
            m = int(sys.argv[2])
            circular_array(n, m)
        except ValueError:
            print("n и m должны быть целыми числами.")