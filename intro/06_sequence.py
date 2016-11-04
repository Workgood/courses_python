#!/usr/bin/env python3
'''
Summarizes elems from 1 to num

Args:
num (int): elems to sum.

Returns:
result (float): sum of all elems.
'''

def sumElems(num):
    cur_fact = 1
    result = 1
    for i in range(1, num + 1):
        cur_fact *= i
        result += 1/cur_fact
    return result


usr_input = int(input("Enter a number of elements to sum: "))
print(sumElems(usr_input))
