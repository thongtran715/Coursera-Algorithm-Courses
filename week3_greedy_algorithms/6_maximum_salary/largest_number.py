#Uses python3

import sys

def largest_number(a):
    #write your code here
    res = []
    while a:
        largest = index = largestFirstDigit = 0
        for i, v in enumerate(a):
            l = int(str(v)[:1])
            if l > largestFirstDigit:
                largest = v
                largestFirstDigit = l
                index = i
            elif l == largestFirstDigit:
                print ("i found ")
        print (largest)
        res.append(largest)
        a.pop(index)
    return res
# if __name__ == '__main__':
#     input = sys.stdin.read()
#     data = input.split()
#     a = data[1:]
#     print(largest_number(a))

# number = [21,2]
number = [91,4,6,1,9]
print (largest_number(number))
