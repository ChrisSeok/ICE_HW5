#4번문제 / C111061 박서연 

def deci2bin(n):
    s = ""
    s_r = ""
    
    while n > 0:
        s = s + str(n%2)
        n = int(n//2)
        
    for c in s:
        s_r = c + s_r
    
    return "0b" + s_r


def main():
    x = int(input("10진수: "))
    print(deci2bin(x))
    
    
main()
    

