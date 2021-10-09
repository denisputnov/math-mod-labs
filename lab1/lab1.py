import matplotlib.pyplot as plt
import json
import argparse

DATA_FILE_PATH = './data.json'


class Plotter:
    def __init__(self, data_path) -> None:
        self.data = self._parse_json_data(data_path)
        self.fig, self.ax = plt.subplots()

    def _parse_json_data(self, data_path):
        with open(data_path, 'r') as f:
            data = json.load(f)

        def parse_string_to_values(string):
            return list(map(float, string.split()))

        for label in data:
            data[label]["x"] = parse_string_to_values(data[label]["x"])
            data[label]["y"] = parse_string_to_values(data[label]["y"])
        return data

    def _plot(self, x, y, label):
        self.ax.scatter(x, y, label=label)
        # ax.plot(x, y, label=label)
        self.ax.set_xlabel('Значение по X')
        self.ax.set_ylabel('Значение по Y')
        self.ax.set_title('Поточечный график')
        self.ax.legend()

    def _show_figure(self):
        plt.show()

    def plot_all(self):
        self.plot_range(0, len(self.data.items()) - 1)

    def plot_index(self, index):
        label, cords = list(self.data.items())[index]
        self._plot(cords["x"], cords["y"], label)
        self._show_figure()

    def plot_range(self, start, end):
        print(start, end)
        for label, cords in list(self.data.items())[start: end + 1]:
            self._plot(cords["x"], cords["y"], label)
        self._show_figure()

    def plot_group(self, index_array):
        data = list(self.data.items())
        for label, cords in [data[index] for index in index_array]:
            self._plot(cords["x"], cords["y"], label)
        self._show_figure()


def main():
    parser = argparse.ArgumentParser(description='Plot graphs')
    parser.add_argument('-a', '--all', help="Show all graphs", required=False, action='store_true')
    parser.add_argument('-o', '--one', help="Show one graph", required=False)
    parser.add_argument('-r', '--range', help="Show range of graphs", required=False)
    parser.add_argument('-g', '--group', help="Show group of graphs", required=False)
    args = parser.parse_args()

    plotter = Plotter(DATA_FILE_PATH)

    if args.all:
        return plotter.plot_all()

    if args.one:
        return plotter.plot_index(int(args.one) - 1)

    if args.range:
        start, end = [int(value) - 1 for value in args.range.split('-')]
        return plotter.plot_range(start, end)

    if args.group:
        index_array = [int(value) - 1 for value in args.group.split('-')]
        return plotter.plot_group(index_array)

    print("Неожиданная ошибка в параметрах запуска")
    exit(1)


if __name__ == "__main__":
    main()
