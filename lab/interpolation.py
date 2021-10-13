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
    def piecewise_parabolic_interpolation(x, y):
        a0 = []
        a1 = []
        a2 = []
        for i in range(1, len(x)-1):
            a2.append(((y[i+1]-y[i - 1])/((x[i + 1] - x[i - 1])*(x[i + 1] - x[i]))) - 
                        ((y[i] - y[i - 1])/((x[i] - x[i - 1])*(x[i + 1]-x[i]))))
            a1.append((y[i] - y[i - 1] - (a2[i-1] *
                        ((x[i] ** 2) - (x[i - 1] ** 2)))) / (x[i] - x[i - 1]))
            a0.append(y[i - 1] - (a1[i-1] * x[i - 1]) -
                        (a2[i-1] * (x[i - 1] ** 2)))
        return [a0, a1, a2]
