from stack import *
binary = Stack()
decimal_number = int(input('Enter the decimal number: '))
base = int(input('Enter the base to which you wish to convert: '))
while decimal_number > 0:
    binary.push(decimal_number%base)
    decimal_number = decimal_number//base
number=binary.items[::-1]
binary_no = ''.join(str(e) for e in number)
print('Converted value: ' + binary_no)
