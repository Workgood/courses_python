#!/usr/bin/env python3


def sequence_sum(num_elems, base_elem):
    '''Computes the sum of sequence 1 - A + A^2 - ... + (-A)^N.

    Args:
        num_elems (int):   number of elements in sequence.
        base_elem (float): base element of the sequence.

    Returns:
        boolean, float: The sum of the sequnce.
    '''
    result = 1
    accum = 1
    if (num_elems < 0):
        return False, result
    for i in range(1, num_elems+1):
        accum *= (-1) * base_elem
        result += accum
    return [True, result]


num_elems = int(input("Enter number of elements: "))
base_elem = float(input("Enter base element: "))
ok, result = sequence_sum(num_elems, base_elem)
if (ok):
    print(result)
else:
    print("An error has occured")
