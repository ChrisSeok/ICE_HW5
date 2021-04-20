# 2번_B735042_김대겸

# main()함수 선언
def main():
    x = int(input("첫 번째 정수: "))
    y = int(input("두 번째 정수: "))
    print(getGCD(x, y))

# getGCD()함수 선언
def getGCD(x, y):
    if x > y:
        minInput = y
    else:
        minInput = x
    for i in range(minInput, 0, -1):
        if (x % i == 0) and (y % i == 0):
            gcd = i
            break
    return gcd

# main()함수 호출
main()
