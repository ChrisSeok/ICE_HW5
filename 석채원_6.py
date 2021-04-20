#6번, B835193 석채원
def getRange(low,high):
    while 1:
        num = int(input("숫자를 입력하시오(%d에서 %d까지 가능)" %(low,high)))
        if low<=num<=high:
            break;
    
def main():
    value = getRange(0,23)
    print("OK")
main()