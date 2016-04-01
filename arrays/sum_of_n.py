def sum_of_numbers(numbers_to_add):
    try:
        int(numbers_to_add[0])
    except ValueError:
        print('Error: ' + numbers_to_add[0] + ' is not an integer!!')
        return None
    if len(numbers_to_add) == 1:
        total = int(numbers_to_add[0])
    else:
        total = int(numbers_to_add[0]) + sum_of_numbers(numbers_to_add[1:])
    return total
   
numbers_to_add = input('Enter player names....').split(',')
print('Sum: ' + str(sum_of_numbers(numbers_to_add)))
