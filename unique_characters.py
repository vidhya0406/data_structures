string = input('Enter string to check..')
if len(set(string)) == len(string):
    print('UNIQUE!')
else:
    print('Not Unique!')
