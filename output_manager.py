import numpy as np
import matplotlib.pyplot as plt

is_file = False
file_name = ""
file = None
def print_points(points):
    if not is_file:
        print("Значения исходной функции:")
        header = " " * 13
        for i in range(len(points)):
            cur = " " * (13 - len(str(i)))
            cur += str(i)
            header += cur
        print(header)
        xs = " " * 12 + "x"
        for i in range(len(points)):
            cur = " " * (13 - len("{:.3f}".format(points[i].x)))
            cur += "{:.3f}".format(points[i].x)
            xs += cur
        print(xs)
        ys = " " * 12 + "y"
        for i in range(len(points)):
            cur = " " * (13 - len("{:.3f}".format(points[i].y)))
            cur += "{:.3f}".format(points[i].y)
            ys += cur
        print(ys)
    else:
        file.write("Значения исходной функции:\n")
        header = " " * 13
        for i in range(len(points)):
            cur = " " * (13 - len(str(i)))
            cur += str(i)
            header += cur
        file.write(header + "\n")
        xs = " " * 12 + "x"
        for i in range(len(points)):
            cur = " " * (13 - len("{:.3f}".format(points[i].x)))
            cur += "{:.3f}".format(points[i].x)
            xs += cur
        file.write(xs + "\n")
        ys = " " * 12 + "y"
        for i in range(len(points)):
            cur = " " * (13 - len("{:.3f}".format(points[i].y)))
            cur += "{:.3f}".format(points[i].y)
            ys += cur
        file.write(ys + "\n")



def print_approx(title, points, approxes, s, kv_otkl, func, r):
    if not is_file:
        print(title)
        header = " " * 13
        for i in range(len(points)):
            cur = " " * (13 - len(str(i)))
            cur += str(i)
            header += cur
        print(header)
        xs = " " * 12 + "x"
        for i in range(len(points)):
            cur = " " * (13 - len("{:.3f}".format(points[i].x)))
            cur += "{:.3f}".format(points[i].x)
            xs += cur
        print(xs)
        ys = " " * 9 + "φ(x)"
        for i in range(len(points)):
            cur = " " * (13 - len("{:.3f}".format(approxes[i])))
            cur += "{:.3f}".format(approxes[i])
            ys += cur
        print(ys)
        eps = " " * 12 + "ε"
        for i in range(len(points)):
            cur = " " * (13 - len("{:.3f}".format(abs(approxes[i] - points[i].y))))
            cur += "{:.3f}".format(abs(approxes[i] - points[i].y))
            eps += cur
        print(eps)
        print("S = " + "{:.3f}".format(s))
        print("δ = " + "{:.3f}".format(kv_otkl))
        print(func)
        if r is not None:
            print("r = {:.3f}".format(r))
    else:
        file.write(title + "\n")
        header = " " * 13
        for i in range(len(points)):
            cur = " " * (13 - len(str(i)))
            cur += str(i)
            header += cur
        file.write(header + "\n")
        xs = " " * 12 + "x"
        for i in range(len(points)):
            cur = " " * (13 - len("{:.3f}".format(points[i].x)))
            cur += "{:.3f}".format(points[i].x)
            xs += cur
        file.write(xs + "\n")
        ys = " " * 9 + "φ(x)"
        for i in range(len(points)):
            cur = " " * (13 - len("{:.3f}".format(approxes[i])))
            cur += "{:.3f}".format(approxes[i])
            ys += cur
        file.write(ys + "\n")
        eps = " " * 12 + "ε"
        for i in range(len(points)):
            cur = " " * (13 - len("{:.3f}".format(abs(approxes[i] - points[i].y))))
            cur += "{:.3f}".format(abs(approxes[i] - points[i].y))
            eps += cur
        file.write(eps + "\n")
        file.write("S = " + "{:.3f}".format(s) + "\n")
        file.write("δ = " + "{:.3f}".format(kv_otkl) + "\n")
        file.write(func + "\n")
        if r is not None:
            file.write("r = {:.3f}".format(r) + "\n")


def print_approx_error(error_message):
    if not is_file:
        print(error_message)
    else:
        file.write(error_message + "\n")


def print_result(res):
    if not is_file:
        print(res)
    else:
        file.write(res + "\n")


OFFSET = 5


def show_graph(points, results):
    xs, ys, np_res = get_x_y_np(points, results)
    x1, x2, y1, y2 = min(xs), max(xs), min(ys), max(ys)
    bx, by = max(abs(x1), abs(x2)) + OFFSET, max(abs(y1), abs(y2)) + OFFSET
    x = np.linspace(min(xs) - OFFSET, max(xs) + OFFSET, 100)

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)

    plt.grid(True)
    plt.xlim((-bx, bx))
    plt.ylim((-by, by))

    ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('center')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')

    for result in results:
        xt = x
        y = np.vectorize(result[2])
        try:
            y(x)
        except ValueError:
            xt = x[x > 0]
        finally:
            ax.plot(xt, y(xt))


    ax.plot(xs, ys, 'ro')
    plt.legend()

    plt.show()


def get_x_y_np(points, result):
    x = []
    y = []
    reses = []
    for point in points:
        x.append(point.x)
        y.append(point.y)
    for res in result:
        reses.append(res)
    return np.array(x), np.array(y), np.array(reses)


