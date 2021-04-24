#6번 C111152 임종욱

def getRange(x, y) :
    a = int(input('숫자를 입력하시오(%d에서 %d까지 가능) '%(x,y)))
    if x <= a <= y :
        return 0
    else :
        getRange(0, 23)

def main():
 value = getRange(0, 23)
 print("OK")

main()