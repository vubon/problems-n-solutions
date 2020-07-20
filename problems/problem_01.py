sample = {
    "key1": 1,
    "key2": {
        "key3": 1,
        "key4": {
            "key5": 4
        }
    }
}


def helper_function(data: dict, depth=1) -> None:
    """
    :param data:
    :param depth:
    :return: None
    """
    for key, value in data.items():
        print(key, depth)
        if isinstance(value, dict):
            helper_function(value, depth + 1)


def print_depth(data: dict) -> None:
    """
    :param: data: A dictionary data sets
    """
    if isinstance(data, dict):
        helper_function(data)
    else:
        raise TypeError("Please insert valid type of dictionary")


if __name__ == '__main__':
    print_depth(sample)
