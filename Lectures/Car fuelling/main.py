
def main(arr, k):
    i = 0
    currentPosition = 0
    count = 0
    lastIndexGas = 0
    while i < len(arr):
        distance = arr[i] - currentPosition
        if distance > k:
            i -= 1
            if i == lastIndexGas:
                return 0
            currentPosition = arr[i]
            count += 1
            lastIndexGas = i
        else:
            i += 1
    return count

def anotherWay(arr, k):
    numFils = current = 0
    while current < len(arr) - 1:
        lastIndex = current
        while current < len(arr) -1 and arr[current +1] - arr[lastIndex] <= k:
            current += 1
        if current == lastIndex:
            return
        if current< len(arr):
            numFils += 1
    return numFils
arr = [0,200,400,600,800]
k = 200
print (main(arr,k))
print (anotherWay(arr,k))
