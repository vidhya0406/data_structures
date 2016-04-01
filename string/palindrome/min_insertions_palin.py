def minInsertions(string,start,end):
    if start == end-1:
        if string[start] == string[end]: 
            return 0
        else: 
            return  1
    if string[start] == string[end]: 
        return minInsertions(string, start+1, end-1)
    else: 
        return min(minInsertions(string,start, end-1), minInsertions(string, start+1, end))+1

string = 'aba'
if string == ''.join(list(string)[::-1]):
   print('Already a palindrome')
else:
   print(minInsertions(string, 0, len(string)-1))

