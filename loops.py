from DMW import DomainWallMemory
from typing import Callable
from Mapping import Mapping
from math import sqrt

N = 10000
L = 5

def loop1(mapping_function: Callable[[int], int], debug=False):
    mapping = Mapping(N * 3 + 11, mapping_function, debug)
    memory = DomainWallMemory(mapping, debug)
    for _ in range(L):
        for k in range(N):
            memory[N + k]
            memory[2 * N + k + 10]
            memory[2 * N + k + 11]
            memory[k]
    
    return memory.get_total_cost()

def loop2(mapping_function: Callable[[int], int], debug=False):
    mapping = Mapping(N * 4, mapping_function, debug)
    memory = DomainWallMemory(mapping, debug)
    for _ in range(L):
        ii = N
        ipntp = 0

        while True:
            ipnt = ipntp
            ipntp += ii
            ii //= 2
            i = ipntp - 1

            for k in range(ipnt + 1, ipntp, 2):
                i += 1
                memory[k - 1]
                memory[k]
                memory[k + 1]
                memory[2 * N + k]
                memory[2 * N + k + 1]
                memory[i]

            if ii <= 0:
                break

    return memory.get_total_cost()

def loop3(mapping_function: Callable[[int], int], debug=False):
    mapping = Mapping(N * 2, mapping_function, debug)
    memory = DomainWallMemory(mapping, debug)
    for _ in range(L):
        for k in range(N):
            memory[N + k]
            memory[k]
    
    return memory.get_total_cost()

def loop4(mapping_function: Callable[[int], int], debug=False):
    mapping = Mapping(N * 2, mapping_function, debug)
    memory = DomainWallMemory(mapping, debug)
    # @TODO
    
    return memory.get_total_cost()

def loop5(mapping_function: Callable[[int], int], debug=False):
    mapping = Mapping(N * 3, mapping_function, debug)
    memory = DomainWallMemory(mapping, debug)
    for _ in range(L):
        for k in range(1, N):
            memory[k - 1]
            memory[N + k]
            memory[2 * N + k]
            memory[k]

    return memory.get_total_cost()

def loop6(mapping_function: Callable[[int], int], debug=False):
    n = int(sqrt(N))
    mapping = Mapping(n * n + n, mapping_function, debug)
    memory = DomainWallMemory(mapping, debug)
    # @TODO
    for _ in range(L):
        for i in range(1, n):
            memory[i]
            for k in range(i):
                memory[n + i * n + k]
                memory[i - k - 1]

    return memory.get_total_cost()

def loop7(mapping_function: Callable[[int], int], debug=False):
    mapping = Mapping(N * 4 + 6, mapping_function, debug)
    memory = DomainWallMemory(mapping, debug)
    for _ in range(L):
        for k in range(N):
            memory[N + k]
            memory[2 * N + k]
            memory[3 * N + k]
            memory[3 * N + k + 1]
            memory[3 * N + k + 2]
            memory[3 * N + k + 3]
            memory[3 * N + k + 4]
            memory[3 * N + k + 5]
            memory[3 * N + k + 6]
            memory[k]

    return memory.get_total_cost()

def loop8(mapping_function: Callable[[int], int], debug=False):
    mapping = Mapping(N * 2, mapping_function, debug)
    memory = DomainWallMemory(mapping, debug)
    # @TODO
    
    return memory.get_total_cost()

def loop9(mapping_function: Callable[[int], int], debug=False):
    mapping = Mapping(N * 2, mapping_function, debug)
    memory = DomainWallMemory(mapping, debug)
    # @TODO
    
    return memory.get_total_cost()

def loop10(mapping_function: Callable[[int], int], debug=False):
    mapping = Mapping(N * 2, mapping_function, debug)
    memory = DomainWallMemory(mapping, debug)
    # @TODO
    
    return memory.get_total_cost()

def loop11(mapping_function: Callable[[int], int], debug=False):
    mapping = Mapping(N * 2, mapping_function, debug)
    memory = DomainWallMemory(mapping, debug)
    for _ in range(L):
        memory[0]
        memory[N]
        for k in range(1, N):
            memory[k - 1]
            memory[N + k]
            memory[k]
    
    return memory.get_total_cost()

def loop12(mapping_function: Callable[[int], int], debug=False):
    mapping = Mapping(N * 2 + 1, mapping_function, debug)
    memory = DomainWallMemory(mapping, debug)
    for _ in range(L):
        for k in range(N):
            memory[N + k]
            memory[N + k + 1]
            memory[k]
    
    return memory.get_total_cost()

def loop13(mapping_function: Callable[[int], int], debug=False):
    mapping = Mapping(N * 2, mapping_function, debug)
    memory = DomainWallMemory(mapping, debug)
    # @TODO
    
    return memory.get_total_cost()

def loop14(mapping_function: Callable[[int], int], debug=False):
    mapping = Mapping(N * 2, mapping_function, debug)
    memory = DomainWallMemory(mapping, debug)
    # @TODO
    
    return memory.get_total_cost()

def loop15(mapping_function: Callable[[int], int], debug=False):
    mapping = Mapping(N * 2, mapping_function, debug)
    memory = DomainWallMemory(mapping, debug)
    # @TODO
    
    return memory.get_total_cost()

def loop16(mapping_function: Callable[[int], int], debug=False):
    mapping = Mapping(N * 2, mapping_function, debug)
    memory = DomainWallMemory(mapping, debug)
    # @TODO
    
    return memory.get_total_cost()

def loop17(mapping_function: Callable[[int], int], debug=False):
    mapping = Mapping(N * 2, mapping_function, debug)
    memory = DomainWallMemory(mapping, debug)
    # @TODO
    
    return memory.get_total_cost()

def loop18(mapping_function: Callable[[int], int], debug=False):
    mapping = Mapping(N * 2, mapping_function, debug)
    memory = DomainWallMemory(mapping, debug)
    # @TODO
    
    return memory.get_total_cost()

def loop19(mapping_function: Callable[[int], int], debug=False):
    mapping = Mapping(N * 3, mapping_function, debug)
    memory = DomainWallMemory(mapping, debug)
    for _ in range(L):
        for k in range(N):
            memory[N + k]
            memory[2 * N + k]
            memory[k]
            memory[k]

        for i in range(1, N):
            k = N - i
            memory[N + k]
            memory[2 * N + k]
            memory[k]
            memory[k]
    
    return memory.get_total_cost()

def loop20(mapping_function: Callable[[int], int], debug=False):
    mapping = Mapping(N * 2, mapping_function, debug)
    memory = DomainWallMemory(mapping, debug)
    # @TODO
    
    return memory.get_total_cost()

def loop21(mapping_function: Callable[[int], int], debug=False):
    mapping = Mapping(N * 2, mapping_function, debug)
    memory = DomainWallMemory(mapping, debug)
    # @TODO
    
    return memory.get_total_cost()

def loop22(mapping_function: Callable[[int], int], debug=False):
    mapping = Mapping(N * 5, mapping_function, debug)
    memory = DomainWallMemory(mapping, debug)
    for _ in range(L):
        for k in range(N):
            memory[N + k]
            memory[2 * N + k]
            memory[3 * N + k]
            memory[4 * N + k]
            memory[k]

    return memory.get_total_cost()

def loop23(mapping_function: Callable[[int], int], debug=False):
    mapping = Mapping(N * 2, mapping_function, debug)
    memory = DomainWallMemory(mapping, debug)
    # @TODO
    
    return memory.get_total_cost()

def loop24(mapping_function: Callable[[int], int], debug=False):
    mapping = Mapping(N, mapping_function, debug)
    memory = DomainWallMemory(mapping, debug)
    for _ in range(L):
        for k in range(1, N):
            memory[k]
    
    return memory.get_total_cost()

implemented = (loop1, loop2, loop3, loop5, loop7, loop11, loop12, loop19, loop22, loop24)
