#8번, B835193 석채원

#convertChar함수 이용
def convertChar(c):
    UpperCase = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    LowerCase = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    
    if (c in UpperCase): 
        for i in range(0,26):
            if(UpperCase[i]==c):
                return LowerCase[i]
                break
    else:
        for i in range(0,26):
            if(LowerCase[i]==c):
                return UpperCase[i]
                break


def convertString(string):
    convStr = ''
    length = len(string) #원래는 len-1해야 하지만 range함수는 두번째인자 전까지 index가 올라가므로 -1은 안해도 된다.
    for i in range(0,length):
        convStr=convStr+convertChar(string[i])
        
    return convStr
        
def main():
 string = input("문자열을 입력하시오?")
 print(convertString(string))
main()
