# Uses python3
import sys
import timeit

# Naive implementation
# Implement quicksort
# Fill knapsack with most valuable item first,
# Then fill knapsack with second most valuable item (if it fits),
# Last, some variation of least valuable item,


def get_optimal_value(capacity, weights, values):
    value = 0.
    # write your code here

    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    # start_time = timeit.default_timer()
    print("{:.10f}".format(opt_value))
    # print(timeit.default_timer() - start_time)
