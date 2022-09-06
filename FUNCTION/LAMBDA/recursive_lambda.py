"""One method for creating recursive lambda functions
   involves assigning the function to a variable and then
   referencing that variable within the function itself
""" 
# Sum of n natural number using lambda recursion
lambda_sum_of_natural_number = lambda x : 1 if x == 0 or x == 1 else x + lambda_sum_of_natural_number(x - 1)
print(lambda_sum_of_natural_number(5)) # This should return 15

# Factorial of n number using recursion

factorial = lambda x : 1 if x == 0 or x == 1 else x * factorial(x - 1)
print(factorial(7)) # This should return 5040