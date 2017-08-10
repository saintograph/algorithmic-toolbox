# Uses python3
import sys
import timeit

# Naive solution
# Divide by 10, get remainder (then subtract remainder from original number then divide again
# to get the number of 10s it took to divide the number by)
# Divide by 5, get remainder (then subtract remainder from original number then divide again
# to get the number of 5s it took to divide the number by)
# Divide by 1

# Naive implementation
def get_change(m):
    # m = m // 10
    i = m // 10
    if m < 6:
        i = m
        return i
    m = m % 10
    if m >= 6:
        m = m % 5
        i = i + 1
        if m != 0:
            i = i + m
            return i
    else:
        if m == 5:
            i = i + 1
            return i
        else:
            i = i + m
            return i
    return i

if __name__ == '__main__':
    # m = int(sys.stdin.read())
    m = int(input())
    # start_time = timeit.default_timer()
    print(get_change(m))
    # print(timeit.default_timer() - start_time)
