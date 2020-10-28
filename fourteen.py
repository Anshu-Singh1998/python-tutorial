# let us c
# A positive number is entered through the keyboard. write a function
# to obtain the prime factors of this number.

def print_factors(n):
    print("The factors of", n, "are:")
    i = 1
    for i in range(1, n + 1):
        if n % i == 0:
            print(i)


num = int(input("Enter a number to find out its prime factor:"))

print_factors(num)
