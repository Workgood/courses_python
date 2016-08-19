def is_prime(num):
    for i in range(2, int(num)):
        if num % i == 0:
            return False
    return True
def count_index(index):
    cur_number = 2
    cur_index = 1
    while cur_index < index:
        if is_prime(cur_number):
            cur_index += 1 
        cur_number += 1
    return cur_number
index = int(input("Enter a number of prime: "))
print(count_index(index))


