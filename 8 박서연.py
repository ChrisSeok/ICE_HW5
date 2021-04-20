#8번문제 / C111061 박서연 

def convertString(string):
    s1 = "abcdefghijklmnopqrstuvwxyz"
    s2 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    r_str = ""
    
    for c in string:
        count1 = 0
        count2 = 0
        
        for d in s1:
            if d == c:
                r_str = r_str + s2[count1]
                break
            else:
                count1 = count1 + 1
        
        for e in s2:
            if e == c:
                r_str = r_str + s1[count2]
                break
            else:
                count2 = count2 + 1
        
    return r_str


def main():
    string = input("문자열을 입력하시오? ")
    print(convertString(string))


main()
    
        
        
        
    
    
   

    
    
