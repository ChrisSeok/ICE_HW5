#7번  C111152 임종욱

def convertChar(c) :
    L = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    l = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    
    #들어온 문자가 대소문자인지 구별한다
    if 'A' <= c <= 'Z':
        # L(i)에 해당하는 문자의 소문자는  l(i) 이다     
        for i in range(len(L)):
            if c == L[i]:
                c= l[i]
             
            
    elif  'a' <= c <= 'z':
        #
        for i in range(len(l)):
            if c == l[i]:
                c= L[i]
                
    return c
    


def main():
 char = input("문자를 입력하시오?")
 print(convertChar(char))

main()
