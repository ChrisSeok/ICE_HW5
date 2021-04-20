# 3번_B735042_김대겸

# 소수 판별 함수 isPrime(n) 선언
def isprime(n):
    for i in range(2, n):
        if (n % i == 0):
            return False
    return True
# 사용자로부터 정수 입력받기
intUser = int(input("정수 입력하시오: "))
# 2부터 사용자로부 입력받은 정수 사이의 소수 출력
for i in range(2, intUser + 1):
    if (isprime(i) == True):
        print(i, end=' ')
