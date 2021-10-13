import json


def parse_json_data(data_path):
    with open(data_path, 'r') as f:
        data = json.load(f)

    def parse_string_to_values(string):
        return list(map(float, string.split()))

    for label in data:
        data[label]["x"] = parse_string_to_values(data[label]["x"])
        data[label]["y"] = parse_string_to_values(data[label]["y"])

    for label in data:
        cords = list(zip(data[label]["x"], data[label]["y"]))
        sorted_cords = sorted(cords, key=lambda values: values[0])
        sorted_x = [cord[0] for cord in sorted_cords]
        sorted_y = [cord[1] for cord in sorted_cords]
        data[label]["x"] = sorted_x
        data[label]["y"] = sorted_y

    return data
