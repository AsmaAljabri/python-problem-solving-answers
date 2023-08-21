# problem [F]
"""
The problem description:

At Al-Azhar, there is an array consisting of a number of integers. They want you to help them 
identify the numbers that appear 3 times in the array they have. Write a program to assist Al-Azhar 
in solving this problem by printing the numbers that appear 3 times in the array.

Note: The given array contains at least one number that appears 3 times.

Input Description:

The input consists of two lines. The first line contains the variable "x" where 5≤n≤10^5
, which is the number of elements in the array. The second line contains "n" integers representing the 
elements of the array. The values of these integers range from 0 to 10000.

"""
n = int(input("Enter the number of elements in the array (n): "))
if n < 5 or n > 10**5:
    print("Invalid input")
else:
    arr_n = list(map(int, input("Enter the elements of the array with spaces: ").split()))
    if len(arr_n) != n:
        print("Invalid input")
    else:
        occ_count = {}
        for num in arr_n:
            occ_count[num] = occ_count.get(num, 0) + 1

        result_numbers = [num for num, count in occ_count.items() if count == 3]

        if len(result_numbers) > 0:
            print("Numbers that repeat 3 times", result_numbers)
        else:
            print("No numbers ")
