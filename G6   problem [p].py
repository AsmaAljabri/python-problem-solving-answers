"""
Problem P - Names and Books

Asmaa went to the library and bought a collection of books, the total number of which is n. Asmaa wants to read all the books she bought, but she can only finish a certain number of books each day. What is the number of days Asmaa will need to finish reading all the books she bought?

Input Description:

The input consists of a single line containing two integers. The first integer represents the total number of books Asmaa bought, n, and the second integer represents the number of books Asmaa can read per day.

Translated to English, the problem statement remains the same.

"""
# PROBLEM [P]
n = int (input("Enter the total number of books = "))
x = int(input("Enter the number of books read per day = "))

if n <= 0 or x <= 0:
    print("numbers must be greater than 0.")
else:
    
    # Number of days = Total number of books / Number of books read per day
    days_to_read_all_books = n // x
    if n % x != 0:
        days_to_read_all_books += 1

    print("Number of days to finish reading all the books:", days_to_read_all_books)
