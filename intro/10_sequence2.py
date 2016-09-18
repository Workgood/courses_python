def sum(N,A):
    result = 1
    pow = 1
    Z = -1
    for i in range(1,N+1):
        pow *= A
        pow *= Z
        result += pow
    return result

N = int(input("Enter N: "))
A = int(input("Enter A: "))
print(sum(N,A))

         
