#Factorial function implementing recursion.
def factorial(num):
    if num == 0:
        return 1

    return num * factorial(num-1)

#Prompting the user for a number.
number = int(input("Enter the number to find the factorial of: "))

#Calling the function and printing the result
print(factorial(number))