#2번문제 / C111061 박서연 

def getGCD(x, y):
    if x > y:
        x, y = y, x
    
    for i in range(y+1, 1, -1):
        if x%i == 0 and y%i == 0:
            return i
            break


def main():
    x = int(input("첫 번째 정수: "))
    y = int(input("두 번째 정수: "))
    print(getGCD(x, y))
    

main()
            