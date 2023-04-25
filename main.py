import numpy as np

import output_manager
from input_manager import is_terminal, get_points_from_console, is_terminal_out, get_points_from_file
from output_manager import print_points, print_result, show_graph
from solver import approx_linear, approx_second_polynomial, approx_third_polynomial, approx_pow, approx_exp, approx_log
if __name__ == '__main__':
    is_terminal = is_terminal()
    is_terminal_out = is_terminal_out()
    results = []
    points = []
    np_points = None
    if is_terminal == "":
        points = get_points_from_console()
        np_points = np.array(points)
    else:
        in_file = open(is_terminal, "r")
        points = get_points_from_file(in_file)
        if points is None:
            exit(-1)
        np_points = np.array(points)

    if is_terminal_out != "":
        output_manager.is_file = True
        output_manager.file_name = is_terminal_out
        output_manager.file = open(is_terminal_out, "w")

    print_points(np_points)
    results.append(approx_linear(np_points))
    results.append(approx_second_polynomial(np_points))
    results.append(approx_third_polynomial(np_points))
    results.append(approx_pow(np_points))
    results.append(approx_exp(np_points))
    results.append(approx_log(np_points))

    mn = 100000000000000
    mn_f = ""
    for i in range(len(results)):
        if results[i][0] >= 0 and results[i][0] < mn:
            mn = results[i][0]
            mn_f = results[i][1]


    res = "Лучше всего опроксимирует " + mn_f + ", δ = {:.3f}".format(mn)
    print_result(res)
    show_graph(points, results)





