#7번, B835193 석채원
def convertChar(c):
    #List 이용
    UpperCase = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    LowerCase = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    
    if (c in UpperCase): #입력이 대문자일 경우
        for i in range(0,26):
            if(UpperCase[i]==c):
                return LowerCase[i]
                break
    else:
        for i in range(0,26):
            if(LowerCase[i]==c):
                return UpperCase[i]
                break
    
def main():
 char = input("문자를 입력하시오?")
 print(convertChar(char))
main()
