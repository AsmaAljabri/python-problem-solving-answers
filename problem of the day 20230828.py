def first_non_repeating_char(s):
    arr_coun = {}
    
    # loop to Count the occurrences of each character
    for i in s:
        if i in arr_coun:
            arr_coun[i] += 1
        else:
            arr_coun[i] = 1
    
    # for loop to Find the first non-repeating character
    for i in s:
        if arr_coun[i] == 1:
            return i
    
    # non-repeating character is found, will return ""
    return ""

# Example usage
s = "hello"
output = first_non_repeating_char(s)
print("Output =", output)  # Output = "h"
