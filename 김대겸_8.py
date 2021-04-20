#8번_B735042_김대겸

# main()선언 (사용자로부터 문자열를 입력받고 convertString(string)을 호출하고 그 결과를 출력하는 함수)
def main():
    string = input("문자열를 입력하시오?")
    print(convertString(string))

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

# convertString(string)선언 (영문 알파벳 문자열을 받아 문자열 내의 대문자는 소문자로, 소문자는 대문자로 바꾸는 함수)
def convertString(string):
    changed = ""
    for ch in string:
        changed = changed + convertChar(ch)
    return changed    

# main() 호출
main()