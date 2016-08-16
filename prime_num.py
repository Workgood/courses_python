def is_prime(num):
    for i in range(2, int(num)):
        if num % i == 0:
            return False
    return True
def count_prime(count):
    prime_numbers = [2]
    next_number = 3
    while len(prime_numbers) < count:
        if is_prime(next_number):
            prime_numbers.append(next_number)
        next_number += 1
    return prime_numbers[-1]
count = int(input("Enter a number of prime: "))
print(count_prime(count))

    
