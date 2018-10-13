# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    value = 0.
    # write your code here
    values = [ value/ weight for value , weight in zip(values,weights)]
    while capacity != 0:
        max = 0
        index = 0
        if len(values) == 0:
            return round(value,4)
        for i , v in enumerate(values):
            if max < v:
                max = v
                index = i
        weight = weights[index]
        if capacity >= weight:
            capacity -= weight
            value += (max*weight)
        else:
            value += (max)*capacity
            capacity = 0
        weights.pop(index)
        values.pop(index)
    return round(value,4)

# capacity = 1000
# values = [500]
# weights = [30]
# print(get_optimal_value(capacity,weights, values))
#


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
