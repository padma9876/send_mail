def factorial(n):
    if n == 0:
       return 1
    else:
       return n * factorial( n -1 )
      
number = 10
result = factorial(number)
print(f"the factorial pf {number} is {result}.")
