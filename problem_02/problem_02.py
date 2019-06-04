class Person(object):
    def __init__(self, first_name, last_name, father):
        self.first_name = first_name
        self.last_name = last_name
        self.father = father


person_a = Person("User", "1", None)
person_b = Person("User", "2", person_a)

a = {
    "key1": 1,
    "key2": {
        "key3": 1,
        "key4": {
            "key5": 4,
            "user": person_b,
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
        elif isinstance(value, Person):
            helper_function(value.__dict__, depth + 1)


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
