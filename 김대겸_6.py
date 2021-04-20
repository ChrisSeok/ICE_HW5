#6번_B735042_김대겸

# main() 선언 (getRange(low, high)의 반환값을 변수value에 저장하고 "OK" 출력함)
def main():
    value = getRange(0, 23)
    print("OK")

# 사용자가 low부터 high까지의 정수를 입력하도록 강제하는 함수 getRange(low, high) 선언.
def getRange(low, high):
    while True: 
        intInput = int(input("숫자를 입력하시오(0에서 23까지 가능)" ))
        if (intInput >= low) and (intInput <= high):
            break
    return intInput
    

# main() 호출
main()
