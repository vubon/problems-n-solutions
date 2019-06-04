a = {
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


def print_depth(data):
    """
    :param: data: A dictionary data sets
    """
    if isinstance(data, dict):
        helper_function(data)
    else:
        raise TypeError("Please insert valid type of dictionary")


# when you will run the test case , please comment out  below line
# print_depth(a)
