import math

import numpy as np
from output_manager import print_approx, print_approx_error

def get_x_y_np(points):
    x = []
    y = []
    for point in points:
        x.append(point.x)
        y.append(point.y)
    return np.array(x), np.array(y)


def approx_linear(points):
    title = "Линейная апроксимация:"
    np_x, np_y = get_x_y_np(points)
    SX = np.sum(np_x)
    SXX = np.sum(np_x ** 2)
    SY = np.sum(np_y)
    SXY = np.sum(np_x * np_y)
    n = len(points)

    delta = SXX * n - SX ** 2
    delta1 = SXY * n - SX * SY
    delta2 = SXX * SY - SX * SXY
    a = delta1 / delta
    b = delta2 / delta
    res = calc_linear_function(a, b, np_x)
    s = np.sum((np_y - res) ** 2)
    r = np.sum((np_x - np.average(np_x)) * (np_y - np.average(np_y))) / \
        np.sqrt(np.sum((np_x - np.average(np_x)) ** 2) * np.sum((np_y - np.average(np_y)) ** 2))
    np_res = np.array(res)
    kv_otkl = np.sqrt(np.sum((np_res - np_y) ** 2) / n)
    func = "φ(x) = {:.3f} * x + {:.3f}".format(a, b)
    print_approx(title, points, np_res, s, kv_otkl, func, r)
    return [kv_otkl, "линейная функция", lambda x: a * x + b]


def approx_second_polynomial(points):
    title = "Квадратичная аппроксимация:"
    np_x, np_y = get_x_y_np(points)
    pf = np.polyfit(np_x, np_y, 2)
    ps = np.poly1d(pf)(np_x)
    s = np.sum((ps - np_x) ** 2)
    n = len(points)
    kv_otkl = np.sqrt(s / n)
    func = "φ(x) = {:.3f}*x^2 + {:.3f} * x + {:.3f}".format(pf[0], pf[1], pf[2])
    print_approx(title, points, ps, s, kv_otkl, func, None)
    return [kv_otkl, "квадратичная функция", lambda x: pf[0] * x ** 2 + pf[1] * x + pf[2]]


def approx_third_polynomial(points):
    title = "Кубическая аппроксимация:"
    np_x, np_y = get_x_y_np(points)
    pf = np.polyfit(np_x, np_y, 3)
    ps = np.poly1d(pf)(np_x)
    s = np.sum((ps - np_x) ** 2)
    n = len(points)
    kv_otkl = np.sqrt(s / n)
    func = "φ(x) = {:.3f} * x^3 + {:.3f} * x^2 + {:.3f} * x + {:.3f}".format(pf[0], pf[1], pf[2], pf[3])
    print_approx(title, points, ps, s, kv_otkl, func, None)
    return [kv_otkl, "кубическая функция", lambda x: pf[0] * x ** 3 + pf[1] * x ** 2 + pf[2] * x + pf[3]]

def approx_pow(points):
    title = "Степенная аппроксимация"
    np_x, np_y = get_x_y_np(points)
    if len(np_x[np_x <= 0]) == 0 and len(np_y[np_y <= 0]) == 0:
        XS, YS = np.log(np_x), np.log(np_y)
        A, B = np.polyfit(XS, YS, 1)[:]
        a, b = math.exp(A), B
        ps = a * np_x ** b

        s = np.sum((ps - np_y) ** 2)
        n = len(points)
        kv_otkl = np.sqrt(s / n)
        func = "φ(x) = {:.3f} * x^{:.3f}".format(a, b)
        print_approx(title, points, ps, s, kv_otkl, func, None)
        return [kv_otkl, "степенная функция", lambda x: a * x ** b]
    else:
        print_approx_error("Невозможно аппроксимировать степенной функцией, т.к. среди значений y есть неположительные")
        return [-1, ""]


def approx_exp(points):
    title = "экспоненциальная аппроксимация"
    np_x, np_y = get_x_y_np(points)
    if len(np_y[np_y <= 0]) == 0:
        YS = np.log(np_y)
        A, B = np.polyfit(np_x, YS, 1)[:]
        a, b = math.exp(A), B
        ps = a * np.exp(b * np_x)

        s = np.sum((ps - np_y) ** 2)
        n = len(points)
        kv_otkl = np.sqrt(s / n)
        func = "φ(x) = {:.3f} * e^{:.3f} * x".format(a, b)
        print_approx(title, points, ps, s, kv_otkl, func, None)
        return [kv_otkl, "экспоненциальная функция", lambda x: a * math.e ** (b * x)]
    else:
        print_approx_error("Невозможно аппроксимировать экспоненциальной функцией, т.к. среди значений y есть неположительные")
        return [-1, ""]


def approx_log(points):
    title = "логарифмическая аппроксимация"
    np_x, np_y = get_x_y_np(points)
    if len(np_x[np_x <= 0]) == 0:
        XS = np.log(np_x)
        A, B = np.polyfit(XS, np_y, 1)[:]
        a, b = A, B
        ps = a * np.log(np_x) + b
        s = np.sum((ps - np_y) ** 2)
        n = len(points)
        kv_otkl = np.sqrt(s / n)
        func = "φ(x) = {:.3f} * ln(x) + {:.3f}".format(a, b)
        print_approx(title, points, ps, s, kv_otkl, func, None)
        return [kv_otkl, "логарифмическая функция", lambda x: a * math.log(x) + b]
    else:
        print_approx_error("Невозможно аппроксимировать логарифмичесокй функцией, т.к. среди значений y есть неположительные")
        return [-1, ""]


def calc_linear_function(a, b, xs):
    res = []
    for i in range(len(xs)):
        res.append(a * xs[i] + b)
    return np.array(res)
