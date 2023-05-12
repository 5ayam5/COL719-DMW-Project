from Mapping import Mapping

class DomainWallMemory:
    def __init__(self, mapping: Mapping, debug=False):
        self.mapping = mapping
        self.size = len(mapping)
        self.debug = debug
        self.ptr = 0
        self.cost = 0
    
    def __getitem__(self, key: int):
        if key >= self.size:
            raise IndexError(f"Index out of range: {key}")
        key = self.mapping[key]
        if self.debug:
            print("Accessing index %d" % key)
        cost = abs(key - self.ptr)
        self.cost += cost
        self.ptr = key
        return cost
    
    def __len__(self):
        return self.size

    def get_total_cost(self):
        return self.cost
