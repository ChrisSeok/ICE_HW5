#6번문제 / C111061 박서연 

def getRange(low, high):
    number = int(input("숫자를 입력하시오(%d에서 %d까지 가능) "%(low, high)))
    
    while True:
        if number<low or number>high:
            return getRange(low, high)
        else:
            break


def main():
    value = getRange(0, 23)
    print("OK")
    
    
main()