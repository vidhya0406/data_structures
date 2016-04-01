def array_sum(array, value):
    binmap = {}
    all_possible_pairs = []
    for i in range(len(array)):
        binmap[i] = value - array[i]
    for computed_value,key in binmap.items():
        if computed_value in array:
            pair = []
            pair.append(key+1)
            pair.append(computed_value)
            all_possible_pairs.append(pair)
        else:
            continue
    return all_possible_pairs

print(str(array_sum([1,2,3,4,5,6,7],7)))
print(str(array_sum([12,3,4,67,89,9,0],7)))
