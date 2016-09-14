def fact(num):
    if num == 0:
        return 1
    cur_fact = 1
    for i in range(1, num + 1):
        cur_fact = cur_fact * i
    return cur_fact

def sum(N):
    result = 1
    for i in range(1, N + 1):
        result += 1/fact(i)
    return result


usr_input = int(input("Enter N: "))
print(sum(usr_input))
