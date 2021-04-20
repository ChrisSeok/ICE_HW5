#7번_B735042_김대겸

# main()선언 (사용자로부터 문자를 입력받고 convertChar(char)을 호출하고 그 결과를 출력하는 함수)
def main():
    char = input("문자를 입력하시오?")
    print(convertChar(char))

# convertChar(char)선언 (대문자는 소문자로, 소문자는 대문자로 바꾸는 함수)
def convertChar(char):
    smallLetter = "abcdefghijklmnopqrstuvwxyz"
    bigLetter = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    # char이 소문자일때 대문자로 변환
    if char in smallLetter:
        for i in range(0, len(smallLetter)):
            if (char == smallLetter[i]):
                char = bigLetter[i]
    # char이 대문자일때 소문자로 변환            
    elif char in bigLetter:
        for i in range(0, len(bigLetter)):
            if (char == bigLetter[i]):
                char = smallLetter[i]
    return char

# main() 호출
main()