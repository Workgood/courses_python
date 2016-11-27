def to_doubles(elems):
    result = []
    for elem in elems:
        result.append(float(elem))
    return result

def to_strings(elems):
    result = []
    for elem in elems:
        result.append(str(elem))
    return result


numbers = to_doubles(input("Enter sorted numbers: ").split(" "))
unique_numbers = sorted(list(set(numbers)))
print(" ".join(to_strings(unique_numbers)))
