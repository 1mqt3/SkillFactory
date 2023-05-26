field = [[" "] * 3 for i in range(3)]
def showfield():
    """Выводим игровое поле"""
    print()
    print("    | 0 | 1 | 2 | ")
    print("  --------------- ")
    for i, row in enumerate(field):
        row_str = f"  {i} | {' | '.join(row)} | "
        print(row_str)
        print("  --------------- ")
    print()


def ask():
    """Просим игрока сделать ход, проверяем корректность ввода"""
    while True:
        cords = input("Ходит: ").split()

        if len(cords) != 2:
            print(" Введите 2 координаты! ")
            continue

        x, y = cords

        if not(x.isdigit()) or not(y.isdigit()):
            print(" Введите числа! ")
            continue

        x, y = int(x), int(y)

        if 0 > x or x > 2 or 0 > y or y > 2:
            print(" Координаты вне диапазона! ")
            continue

        if field[x][y] != " ":
            print(" Клетка занята! ")
            continue

        return x, y

def check_win():
    """Проверяем выиграл ли игрок"""
    win_cord = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for cord in win_cord:
        symbols = []
        for pos in cord:
            symbols.append(field[pos[0]][pos[1]])
        if symbols == ["X", "X", "X"]:
            print(" Выиграл X! ")
            return True
        if symbols == ["0", "0", "0"]:
            print(" Выиграл 0! ")
            return True
    return False

def main():
    """Соединяем все функции, запускаем игру"""
    num = 0
    while not check_win():
        showfield()
        num += 1

        if num % 2 == 1:
            print(" Ходит крестик ")
        else:
            print(" Ходит нолик ")

        x, y = ask()

        if num % 2 == 1:
            field[x][y] = "X"
        else:
            field[x][y] = "0"

        if num == 9:
            print(" Ничья! ")
            break

main()