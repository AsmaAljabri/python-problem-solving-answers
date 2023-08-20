# problem [s]
"""
Problem - Ali and the Digits

Ali has been given a positive integer and has been asked to calculate the sum of its individual digits.

For example, given the number: 231, the sum of its digits would be 1 + 3 + 2 = 6.

Input Description:

The first line contains a positive integer representing the number given to Ali, let it be "n".
"""
n = int(input("enter the number"))

total_sum = 0
while n > 0:
    digit = n % 10
    total_sum += digit
    n //= 10
print(total_sum)