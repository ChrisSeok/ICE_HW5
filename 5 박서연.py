#5번문제 / C111061 박서연 

def getSorted(x, y):
    if x > y:
        x, y = y, x
    
    return(x, y)


def main():
    x = int(input("첫 번째 정수: "))
    y = int(input("두 번째 정수: "))
    print(getSorted(x, y))


main()


    
