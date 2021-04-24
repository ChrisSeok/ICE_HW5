#2번  C111152 임종욱

def getGCD(x,y):
    i = 1
    while i <= min(x,y):
        if x % i == 0 and y % i == 0 :   #조건을 만족하면 공약수
            GCD = i
        i += 1
    return GCD

def main():
 x = int(input("첫 번째 정수: "))
 y = int(input("두 번째 정수: "))
 print(getGCD(x, y))


main()
