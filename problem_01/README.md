
1) Write the following function’s body. A nested dictionary is passed as parameter. You need to print all keys with their depth.

Sample Input:
```python
a = {
"key1": 1,
"key2": {
    "key3": 1,
    "key4": {
        "key5": 4
        }
    }
}
```

Sample Output:
```bash
key1 1
key2 1
key3 2
key4 2
key5 3
```
```python
def print_depth(data):
    """
    :param: data
    """
    # Write function body
```
You may write additional function.
