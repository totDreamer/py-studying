def add_to_list_in_dict(data, key, element):
    try:
        data[key].append(element)
    except KeyError:
        data[key] = []
        data[key].append(element)
