from collections import deque

string = input('Enter string to check palindrome..')
if len(string) == 1:
   print('PALINDROME!')
elif string == None:
   print('Input string cannont be empty')
else:
   char_dequeue = deque()
   for char in string:
       char_dequeue.append(char)
   check = True
   while len(char_dequeue) > 1 and  check == True:
       if char_dequeue.popleft() != char_dequeue.pop():
           check = False
           
   if check == True:
       print('Palindrome!')
   else:
       print('Not a palindrome!')

