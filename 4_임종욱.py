#4번 C111152 임종욱

#입력된 10진수를 2진수로 바꾸는 함수
#주어진 10진수를 2로 계속 나누어 나온 나머지를 역으로 나열하면 2진수로 표현한 수이다 
def deci2bin(n):
    bin2 = '0b'
    q = n       #q는 몫
    r = []      #r은 나머지 
    while q >=1  :
        r += [q%2]
        q = q//2
    a = ''         #r의 값을 string으로 변환
    b = ''         # string으로 변환 후 a의 문자열을 뒤집은 
    #r을 문자열로 바꾼다
    for i in r :
        a += str(i)
    #a를 뒤집는다
    for t in a:    
        b = t +b
        
    bin2 += b
    return bin2
       

def main():
 x = int(input("10진수: "))
 print(deci2bin(x))


main()