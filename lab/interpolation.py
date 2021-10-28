import numpy as np


class Interpolation:
    @staticmethod
    def polynomial_interpolation(x, y, xl):
        yl = []
        for xl_value in xl:
            # Полином
            L = 0
            # Во вложенных циклах i == j т.к x и y имеют равную длинну
            for j in range(len(x)):
                # Промежуточные значения полинома. Первоначально предполагаем, что они равны y[i]
                intermediate_polynom_value1 = y[j]
                intermediate_polynom_value2 = y[j]

                for i in range(len(x)):
                    # При i == j pl2 обращается в 0
                    if i == j:
                        continue

                    # Находим числитель и знаменитель для нашего полинома и умножаем все на y[n]
                    intermediate_polynom_value1 = (
                        xl_value - x[i]) * intermediate_polynom_value1
                    intermediate_polynom_value2 = (
                        x[j] - x[i]) * intermediate_polynom_value2
                # Находим значение L[i]
                L = L + (y[j] * (intermediate_polynom_value1 /
                        intermediate_polynom_value2))

            # Добавляем полученное значение полинома для xl_value. Полученный массив вернём из функции как значения по Y
            yl.append(L)

        return yl

    @staticmethod
    def piecewise_linear_interpolation(x_values, y_values, xl):
        res = 0
        for i in range(len(x_values)):
            if x_values[i - 1] <= xl <= x_values[i]:
                x = xl - x_values[i]
                yp = y_values[i] - y_values[i - 1]
                xp = x_values[i] - x_values[i - 1]
                res = y_values[i] + ((yp / xp) * x)
                break
        return res

    @staticmethod
    def piecewise_parabolic_interpolation(x, y, arg):
        res = 0
        for i in range(len(x)-1):
            if arg >= x[i] and arg <= x[i+1]:
                matrix = np.array(
                    [[x[i-1]**2, x[i-1], 1], 
                     [x[i]**2, x[i], 1], 
                     [x[i+1]**2, x[i+1], 1]])
                vector = np.array([y[i-1], y[i], y[i+1]])
                poly = np.linalg.solve(matrix, vector) 
                res = poly[0]*arg**2 + poly[1]*arg + poly[2]
            
        return res
