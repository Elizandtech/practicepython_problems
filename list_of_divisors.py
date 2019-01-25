## Ask the user for a number, print out a list of all the divisors of that number.

def return_divisors_of_a_number(N):
    return [integer for integer in range(1, N+1) if N % integer == 0]

inp_num = int(input("Enter a positive integer: "))
print (return_divisors_of_a_number(inp_num))

