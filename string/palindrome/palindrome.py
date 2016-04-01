from collections import deque

def check_without_deque(string):
   chars = [char for char in string.lower() if char.isalpha()]
   if len(chars) == 0:
       print('No alphabets!!')
       return False
   return (chars == chars[::-1])

string = input('Enter string to check palindrome..')
if len(string) == 1:
   print('PALINDROME!')
else:
   char_dequeue = deque()
   for char in string:
       if char.isalpha():
          alpha_check = True
          char_dequeue.append(char.lower())
       else:
          alpha_check = False
   check = True
   if alpha_check == False:
       print('No alphabets in given phrase!!')

   else:
       while len(char_dequeue) > 1 and  check == True:
           if char_dequeue.popleft() != char_dequeue.pop():
               check = False
   
       if check == True:
           print('Palindrome!')
       else:
           print('Not a palindrome!')

if check_without_deque(string):
    print('Of course a plaindrome!')

else:
    print('Not a palindrome!')
