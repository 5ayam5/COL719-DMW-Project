class DomainWallMemory:
    def DomainWallMemory(self, size):
        self.size = size
        self.mem = [0] * size
        self.ptr = 0
        self.cost = 0
    
    def __getitem__(self, key):
        if key >= self.size:
            raise IndexError("Index out of range")
        self.cost += abs(key - self.ptr)
        self.ptr = key
        return self.mem[key]
    
    def __setitem__(self, key, value):
        if key >= self.size:
            raise IndexError("Index out of range")
        self.cost += abs(key - self.ptr)
        self.ptr = key
        self.mem[key] = value
    
    def __len__(self):
        return self.size

    def get_cost(self):
        return self.cost