from .helper import print_mode_options
from config import DATA_FILE_PATH
from plotter import Plotter


def enable_working_mode():
    print_mode_options()
    mode = input(">>> ")

    if mode not in ['i', 'd']:
        print("Введён неверный аргумент")
        exit(1)

    plotter = Plotter(DATA_FILE_PATH)
    
    if mode == 'd':
        plotter.plot_graph()
    
    if mode == 'i':
        plotter.plot_interpolation()