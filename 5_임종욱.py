#5번 C111152 임종욱

def getSorted(x,y) :
    if x >= y :
        s = '(%d, %d)'%(y,x)
    else :
        s = '(%d, %d)'%(x,y)
    return s

def main():
 x = int(input("첫 번째 정수: "))
 y = int(input("두 번째 정수: "))
 print(getSorted(x, y))


main()
