def fact(num):
    cur_num = 1
    for i in range(num):
        cur_num = cur_num * (i + 1)
    return cur_num

def sum(N):
    cur_sum = 1
    for i in range(1, N + 1):
        cur_sum += 1/fact(i)
    return cur_sum
usr_input = int(input("Enter N: "))
print(sum(usr_input))
