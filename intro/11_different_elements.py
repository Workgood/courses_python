"""
Converts set to list(takes elems from set and put them to list):

Args:
array : set we should convert.
result (list): list wich made from set.

Returns:
ints(return value of strsToInts).
"""
def setToList(array):
    
    def strsToInts(strs):
        ints = []
        for i in strs:
            ints.append(int(i))
        ints = sorted(ints)
        return ints
   
    result = []
    for i in array:
        result.append(i)
    return strsToInts(result)


usr_nums = set(input("Enter some: ").split())
print(setToList(usr_nums))

