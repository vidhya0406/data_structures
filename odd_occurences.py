def getOddOccurrence(arr):
    res = 0
    for element in arr:
        res = res ^ element
    return res
arr = [ 2, 3, 5, 4, 5, 2, 4, 3, 5, 2, 4, 4, 2]
print(getOddOccurrence(arr))
