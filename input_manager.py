from Point import Point


def is_terminal():
    while True:
        try:
            print("Если хотите ввести данные в консоль, введите - 1")
            print("Если хотите прочитать данные из файла, введите - 2")
            res = int(input())
            if res != 1 and res != 2:
                raise Exception()
            if res == 2:
                print("Введите имя файла")
                file_name = input()
                return file_name
            return ""
        except:
            print("Ошибка ввода, попробуйте еще раз")


def is_terminal_out():
    while True:
        try:
            print("Если хотите вывести результаты в консоль, введите - 1")
            print("Если хотите записать результаты в файл, введите - 2")
            res = int(input())
            if res != 1 and res != 2:
                raise Exception()
            if res == 2:
                print("Введите имя файла")
                file_name = input()
                return file_name
            return ""
        except:
            print("Ошибка ввода, попробуйте еще раз")


def get_points_from_console():
    while True:
        try:
            res = []
            print("Введите количество точек (от 8 до 12)")
            count = int(input())
            if count < 8 or count > 12:
                raise Exception
            print("Задайте ", count, " точек")
            for i in range(count):
                print("Введите ", i + 1, " пару x - y")
                x, y = map(float, input().split())
                point = Point(x, y)
                res.append(point)
            return res
        except Exception:
            print("Произошла ошибка во время ввода данных, попробуйте снова")

def get_points_from_file(f):
    try:
        res = []
        count = int(f.readline())
        if count < 8 or count > 12:
            raise Exception
        for i in range(count):
            x, y = map(float, f.readline().split())
            point = Point(x, y)
            res.append(point)
        return res
    except Exception:
        print("Произошла ошибка во время чтения данных из файла, попробуйте снова")

