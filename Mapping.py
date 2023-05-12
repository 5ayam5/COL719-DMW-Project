from typing import Callable

class Mapping:
    def __init__(self, size : int, mapping_function : Callable[[int], int], debug=False):
        self.size = size
        self.mapping_function = mapping_function
        self.debug = debug

    def __getitem__(self, key : int):
        if key >= self.size:
            raise IndexError("Index out of range")
        key = self.mapping_function(key)
        return key

    def __len__(self):
        return self.size
