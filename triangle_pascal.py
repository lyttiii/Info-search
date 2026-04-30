def get_positive_int(prompt="Введите положительное целое число: "):
    while True:
        s = input(prompt).strip()
        if s == "":
            print("Введена пустая строка")
            continue
        try:
            x = float(s)
        except ValueError:
            print("Это не число, введите целое положительное число")
            continue
        if not x.is_integer():
            print("Число не целое, введите целое положительное число")
            continue
        n = int(x)
        if n <= 0:
            print("Число должно быть положительным")
            continue
        return n


def generate_pascals_triangle(n):
    rows = []
    for i in range(n):
        if i == 0:
            rows.append([1])
        else:
            prev = rows[-1]
            middle = [prev[j] + prev[j+1] for j in range(len(prev) - 1)]
            new_row = [1] + middle + [1]
            rows.append(new_row)
    return rows


def print_triangle_centered(rows):
    if not rows:
        return

    last_line = ' '.join(map(str, rows[-1]))
    width = len(last_line)
    for row in rows:
        line = ' '.join(map(str, row))
        print(line.center(width))


def main():
    n = get_positive_int()
    triangle = generate_pascals_triangle(n)
    print("\nРезультат:")
    print_triangle_centered(triangle)

if __name__ == "__main__":
    main()
