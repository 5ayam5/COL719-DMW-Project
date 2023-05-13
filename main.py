import loops
from Mapping import Mapping
import matplotlib.pyplot as plt

def get_mappings():
    maps = []
    
    # Loop 1
    def map1(x, n):
        bin_ = x // n
        if x >= 2 * n:
            bin_ += (x - 2 * n - 10) % 2
            x -= 10
        return 4 * (x % n)  + (1 + bin_) % 4
    maps.append(lambda x: map1(x, loops.N))

    # Loop 2
    def map2(x, n):
        if x == 0:
            return 0
        bin_ = x // (2 * n) + (1 + x) % 2
        return 1 + 2 * (x % n) + bin_
    maps.append(lambda x: map2(x, loops.N))

    # Loop 3
    maps.append(lambda x: 2 * (x % loops.N) + (1 + x // loops.N) % 2)

    # Loop 5
    maps.append(lambda x: 3 * (x % loops.N) + (2 + x // loops.N) % 3)

    # Loop 7
    def map7(x, n):
        bin_ = x // n
        if x >= 3 * n:
            bin_ += (x - 3 * n) % 7
        return 10 * (x % n) + (9 + bin_) % 10
    maps.append(lambda x: map7(x, loops.N))

    # Loop 11
    maps.append(lambda x: 2 * (x % loops.N) + x // loops.N)

    # Loop 12
    def map12(x, n):
        bin_ = x // n
        if x >= n:
            bin_ += (x - n) % 2
        return 3 * (x % n) + (2 + bin_) % 3
    maps.append(lambda x: map12(x, loops.N))

    # Loop 19
    maps.append(lambda x: 3 * (x % loops.N) + (2 + x // loops.N) % 3)

    # Loop 22
    maps.append(lambda x: 5 * (x % loops.N) + (4 + x // loops.N) % 5)

    # Loop 24
    maps.append(lambda x: x)
    
    return maps

if __name__ == "__main__":
    mappings = get_mappings()
    base_costs = []
    optimal_costs = []
    for i, loop in enumerate(loops.implemented):
        print(loop.__name__)
        base = loop(lambda x: x)
        optimal = loop(mappings[i])
        base_costs.append(base)
        optimal_costs.append(optimal)
        print("\tBase cost: %d" % base)
        print("\tOptimal cost: %d" % optimal)
        print("\tImprovement: %f%%" % (100 * (base - optimal) / base))

    plt.figure()
    plt.semilogy(base_costs, label="Base")
    plt.semilogy(optimal_costs, label="Optimal")
    plt.legend()
    plt.xlabel("Loop")
    plt.ylabel("Cost")
    plt.title("Cost of Base and Optimal Implementations")
    plt.savefig("results.png")
    plt.close()
