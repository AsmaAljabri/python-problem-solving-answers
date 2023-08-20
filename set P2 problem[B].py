# problem [B]
"""
Problem B - Factors of a Number

The mathematics teacher has assigned you the following homework. Can you solve it?

You are given an integer N, and you are required to write a program that prints all the factors of the number N in ascending order.

The factors of the number N are all the numbers that can divide N without leaving a remainder.

For example, the factors of the number 6 are: 1, 2, 3, and 6.

Input Description:

The input consists of a single line containing an integer N.

"""
N = int(input("Enter an number N: "))


factors = []
for num in range(1, N +1):
    if N % num == 0:
        factors.append(num)

print("Factors of ", N , "is the factors", factors)

