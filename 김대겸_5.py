#5번_B735042_김대겸

# 사용자로부터 두 개의 정수를 각각 입력받고 getSorted(x, y)를 호출하는 main() 선언
def main():
    x = int(input("첫 번째 정수: "))
    y = int(input("두 번째 정수: "))
    print(getSorted(x, y))
# 두 개의 수를 오름차순으로 반환하는 함수 getSorted(x, y) 선언
def getSorted(x, y):
    if (x > y):
        temp = y
        y = x
        x = temp
    return x, y
# main() 호출
main()
