import matplotlib.pyplot as plt
import json


DATA_FILE_PATH = './data.json'


def parse_json_data(data_path):
    with open(data_path, 'r') as f:
        data = json.load(f)

    def parse_string_to_values(string):
        return list(map(float, string.split())) 
    
    for label in data: 
        data[label]["x"] = parse_string_to_values(data[label]["x"])
        data[label]["y"] = parse_string_to_values(data[label]["y"]) 
    return data


def plot(data, graph_range): 
    start, end = graph_range
    fig, ax = plt.subplots()
    for label, cords in list(data.items())[start : end+1]:
        ax.scatter(cords["x"], cords["y"], label=label)
        # ax.plot(cords["x"], cords["y"], label=label)
        ax.set_xlabel('x label')
        ax.set_ylabel('y label')
        ax.set_title('Simple Plot')
        ax.legend()


def parse_graph_range():
    graph_count = list(map(int, input("Какой график вывести ( -1 чтобы покзаать все )?: ").split()))
    if graph_count[0] == -1 or graph_count[0] < 0:
        return [-1, -1]
    elif (len(graph_count) == 1): 
        start = graph_count[0] - 1
        end = graph_count[0] - 1
    elif(len(graph_count) == 2 and graph_count[1] >= graph_count[0]):
        start = graph_count[0] - 1
        end = graph_count[1] - 1
    else:
        print("Неверно указаны графики. Укажите их в формате <int> или <int> <int> для указания диапазона.")
        exit(1)
    return start, end
    

def main():
    start, end = parse_graph_range()
    data = parse_json_data(DATA_FILE_PATH)

    if start == -1:
        start, end = 0, len(data) - 1
    
    if end > len(data) - 1:
        print("В данных нет такого количества графиков")
        exit(1)

    plot(data, [start, end])
    plt.show()


if __name__ == "__main__": 
    main()
