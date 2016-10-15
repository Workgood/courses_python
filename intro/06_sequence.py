#!/usr/bin/env python3
'''
Function wich summarizes elems from 1 to num

Args:
num (int): number of operations.

Returns:
result (float): sum of all elems.
'''

def SumElems(num):
    cur_fact = 1
    result = 1
    for i in range(1, num + 1):
        cur_fact *= i
        result += 1/cur_fact
    return result


usr_input = int(input("Enter a number of operations: "))
print(SumElems(usr_input))
