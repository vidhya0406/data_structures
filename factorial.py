def factorial(n):
   if n <1:   # base case
       return 1
   else:
       return n * factorial( n - 1 )  # recursive call

fact_of = int(input('Find me factorial of: '))
print('Factorial of ' + str(fact_of) + ' is: ' + str(factorial(fact_of)))
