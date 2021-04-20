#3번문제 / C111061 박서연 

number = int(input("정수 입력하시오: "))

def isPrime(n):
    if n < 2:
        return False
    
    for i in range(2, n):
        if n % i == 0:
            return False
    
    return True

for i in range(number):
    if isPrime(i):
        print(i, "", end="")

    


