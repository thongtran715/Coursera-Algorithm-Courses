# Uses python3
import sys

def get_change(m):
    #write your code here
    coins = [1,5,10]
    count = 0
    largetCoins = -1
    while m != 0:
        if abs(largetCoins) > len(coins):
            return -1
        if m >= coins[largetCoins]:
            m -= coins[largetCoins]
            count += 1
        else:
            largetCoins -= 1
    return count

def topDown(arr, m,cache):
    if m in cache:
        return cache[m]
    if m == 0:
        return 0
    maxVal = float('inf')

    for i in arr:
        if m - i >= 0:
            maxVal = min(topDown(arr, m - i, cache), maxVal)
    cache[m] = maxVal + 1
    return cache[m]

def bottomUp(arr,k):
    dp = [0] * (n+1)
    dp[0] = 0
    dp[1] = 1
    i = 1
    for k in range(2, n+1):
        dp[k] = min(dp[k - x] for x in arr if x <= k) + 1
    return dp[-1]



if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
