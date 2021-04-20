#4번, B835193 석채원
def deci2bin(n):
    bin = '0b'
    i = 0
    while (2**i<=n): # n보다 작거나 같은 최대의 2의 제곱수 구하기
        i+=1         # 원하는 수는 i-1
    for j in range(i-1,-1,-1): #j는 i-1 부터  0 까지 줄여간다 #(start,stop(포함x),step)
        #이진수 계산
        if(n>=(2**j)): 
            bin=bin+'1'
            n-=(2**j)
        else:
            bin=bin+'0'
    return bin
        
        
def main():
 x = int(input("10진수: "))
 print(deci2bin(x))
 
main()