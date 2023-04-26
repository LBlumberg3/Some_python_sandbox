def factorial(num):
    if(num == 0):
        return 1
    elif(num == 1):
        return 1
    else: 
        return num * factorial(num - 1)

def recurisve_sum(number):
    if(number == 0):
        return 0
    if (num == 1):
        return 1
    return number + recurisve_sum(number - 1)


def main():
    print("Factorial of  5 is: " + str(factorial(6)))
    print("Sum of of  5! is: " + str(recurisve_sum(6)))

main()