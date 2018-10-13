# python3
def fibo(n):
    if n <= 1:
        return n
    table = {}
    table[0] = 1
    table[1] = 1
    for i in range(2, n):
        table[i] = table[i-1] + table[i-2]
    return table[n-1]

n = int(input())
print(fibo(n))
