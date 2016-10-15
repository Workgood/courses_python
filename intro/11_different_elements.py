"""
Converts set to list(takes elems from set and put them to list):

Args:
set : set we should convert.
result (list): list wich made from set.

Returns:
StrsToInts(result): function wich converts strings to integers
                    from our list(result) and returns sorted list.
"""
def SetToList(set):
    
    def StrsToInts(strs):
        ints = []
        for i in strs:
            ints.append(int(i))
        ints = sorted(ints)
        return ints
   
    result = []
    for i in set:
        result.append(i)
    return StrsToInts(result)


usr_nums = set(input("Enter some: ").split())
print(SetToList(usr_nums))

