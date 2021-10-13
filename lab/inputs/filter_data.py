from .helper import print_graph_options

def filter_data(data): 
    print_graph_options()
    option = input('>>> ')

    if option not in ['all', 'one', 'range', 'group']:
        print("Введён неверный аргумент")
        exit(1)

    if option == 'all':
        return data
    
    if option == "one":
        index = int(input("Введите индекс графика: ")) - 1
        label, cords = list(data.items())[index]
        return { label: cords }
    
    if option == "range":
        start, end = [value - 1 for value in list(map(int, input("Введите диапазон (2 целых числа через пробел): ").split(' ')))]
        return { label: cords for (label, cords) in list(data.items())[start: end + 1] }

    if option == "group":
        index_array = [value - 1 for value in list(map(int, input("Введите последовательность цифр - индексы графиков через пробел: ").split(' ')))]
        group = [list(data.items())[index] for index in index_array]
        return { label: cords for (label, cords) in group}

