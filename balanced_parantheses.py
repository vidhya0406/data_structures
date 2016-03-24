from stack import *
checker = Stack()
expr_to_check = input('Enter expression to validate: ')
balanced = True
def match(popped):
    if popped == ']':
        return '['
    elif popped == ')':
        return '('
    elif popped == '}':
        return '{'
    else:
        return None

for character in expr_to_check:
    if character in '({[':
        checker.push(character)
    elif character in ')]}':
        if checker.isEmpty():
            balanced = False
        else:
            if match(checker.peek()) != checker.pop():
                balanced = False
    else:
       continue

if checker.isEmpty() and balanced:
    print('BALANCED!')
else:
    print('Not balanced!!')

