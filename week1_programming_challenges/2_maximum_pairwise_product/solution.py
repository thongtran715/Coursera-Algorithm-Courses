# python3

def max_pairwise_product (arr):
    if len(arr) == 0 or len(arr) == 1:
        return 0
    first = arr[0]
    second = -1
    for i in range(1,len(arr)):
        if arr[i] > first:
            second = first
            first = arr[i]
        elif arr[i] <= first:
            if arr[i] >= second:
                second = arr[i]
    product = second * first
    return 0 if product < 0 else product

# def anotherWay (arr):
#     product = 0
#     for i in range(1,len(arr)):
#         for j in range(i+1, len(arr)):
#             product = max(product, arr[i]*arr[j])
#     return product
#
# arr = [2,9,3,1,9]
# print (max_pairwise_product(arr))
# import random
# def stressTest(N, M):
#     while True:
#         n = N
#         arr = []
#         for i in range(n):
#             arr.append(random.randint(1,M))
#         result1 = max_pairwise_product(arr)
#         result2 = anotherWay(arr)
#         if result1 == result2:
#             print ("OK")
#         else:
#             print ("Test case ", arr)
#             print ("Wrong Answer", result1, result2)
#             break
#
#




if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))
