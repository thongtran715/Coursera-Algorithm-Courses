# Uses python3
import sys
def get_fibonacci_huge_naive(n,m):
    if n <=1:
        return n
    first = second = 1
    for i in range(2,n):
        temp = second + first
        first = second
        second = temp
    return second % m

if __name__ == '__main__':
    input = sys.stdin.read();
    n, m = map(int, input.split())
    print(get_fibonacci_huge_naive(n, m))
