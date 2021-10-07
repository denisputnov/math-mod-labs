from numpy import random
import json


NUMBER_OF_GRAPHS = 5
VALUES_COUNT = 20


def ordinal(num):
	SUFFIXES = {1: 'st', 2: 'nd', 3: 'rd'}

	if 10 <= num % 100 <= 20:
		suffix = 'th'
	else:
		suffix = SUFFIXES.get(num % 10, 'th')

	return str(num) + suffix


def get_random_cords():
	x = ' '.join([str(x) for x in range(1, VALUES_COUNT + 1)])
	y = ' '.join(list(map(str, random.randint(20, size=(VALUES_COUNT)))))
	return [x, y]


def generate_data():
	data = dict()
	labels = [ordinal(x) for x in range(1, NUMBER_OF_GRAPHS + 1)]
	for label in labels:
		x, y = get_random_cords()
		data[label] = {"x": x, "y": y}

	return data


def save_to_json(data):
	with open('generated.json', 'w') as outfile:
		json.dump(data, outfile)

def main():
	data = generate_data()
	save_to_json(data)


if __name__ == "__main__":
	main()

