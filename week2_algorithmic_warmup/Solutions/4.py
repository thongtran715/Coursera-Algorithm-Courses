# Uses python3
import sys
def gcd_naive(a, b):
    while (b):
        a, b = b, a % b
    return a


def lcm(x, y):
   """This function takes two
   integers and returns the L.C.M."""
   lcm = (x*y)//gcd_naive(x,y)
   return lcm

if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm(a, b))
