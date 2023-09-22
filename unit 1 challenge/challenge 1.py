def num_bers(n):

    if n==0 or n==1:

        return 1

    else:

        return n*num_bers(n-1)

number = int(input("Enter a value : "))

res = num_bers(number)

print("The factorial of {} is {}.".format(number, res))
