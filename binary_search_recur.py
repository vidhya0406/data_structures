def binarySearch(alist, item):
    print('Searching in: ' + str(alist))
    if len(alist) == 0:
        return False
    else:
        midpoint = len(alist)//2
        print('Mid point: ' + str(midpoint) + ' Value: ' + str(alist[midpoint]))
        if alist[midpoint]==item:
            return True
        else:
            if item < alist[midpoint]:
                return binarySearch(alist[:midpoint],item)
            else:
                return binarySearch(alist[midpoint+1:],item)
list_to_search = input('Search data: ').split(',')
list_to_search = [int(i) for i in list_to_search]
find_me = int(input('Find me: '))
print(str(binarySearch(list_to_search, find_me)))
