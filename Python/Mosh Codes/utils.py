def find_max(list):
    max_value = list[0]
    for item in list:
        if item > max_value:
            max_value = item
    return max_value

