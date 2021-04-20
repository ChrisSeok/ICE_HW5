#7번문제 / C111061 박서연 

def convertChar(c):
    s1 = 'abcdefghijklmnopqrstuvwxyz'
    s2 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    count1 = 0
    count2 = 0
    
    for c in s1:
        if c == char:
            return s2[count1]
        else:
            count1 = count1 + 1
        
    for c in s2:
        if c == char:
            return s1[count2]
        else:
            count2 = count2 + 1
            

def main():
    global char
    char = input("문자를 입력하시오?")
    print(convertChar(char))
    

smain()