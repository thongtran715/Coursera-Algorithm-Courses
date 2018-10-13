# Uses python3
import sys

def fibonacci_sum_naive(n):
    if n <= 1:
        return n
    previous = 0
    current  = 1
    second = 1
    for i in range(n - 1):
        previous, current = current, previous + current
        if i == 2:
            second = current

    return (current- second)%10
#
# if __name__ == '__main__':
#     input = sys.stdin.read()
#     n = int(input)
#     print(fibonacci_sum_naive(n))
n = 100
print (fibonacci_sum_naive(n+2))
