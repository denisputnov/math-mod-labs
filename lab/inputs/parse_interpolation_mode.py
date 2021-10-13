from .helper import print_interpolation_mods


def parse_interpolation_mode():
    print_interpolation_mods()
    mode = input(">>> ")

    if mode not in ['1', '2', '3', '4']:
        print("Введён неверный аргумент")
        exit(1)
    
    return mode