# Uses python3
import sys

def fibonacci_sum_naive(n):
    if n <= 1:
        return n
    previous = 1
    current  = 1
    second = 1
    for i in range(2,n):
        previous, current = current, previous + current
    return (current- 1)%10

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(fibonacci_sum_naive(n+2))
