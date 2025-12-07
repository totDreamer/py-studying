def get_min_max(data):
    if not data:
        return None

    num_data = dict(enumerate(data))
    return (min(num_data, key=lambda x: num_data[x]), max(num_data, key=lambda x: num_data[x]))

data = [2, 3, 8, 1, 7]

print(get_min_max(data))


data = [1, 1, 2, 3, 8, 8]

print(get_min_max(data))