'''
def fact(num):
    if num == 0:
        return 1
    cur_fact = 1
    for i in range(1, num + 1):
        cur_fact = cur_fact * i
    return cur_fact
'''

def sum(N):
    cur_fact = 1
    result = 1
    for i in range(1, N + 1):
        cur_fact *= i
        result += 1/cur_fact
    return result


usr_input = int(input("Enter N: "))
print(sum(usr_input))
