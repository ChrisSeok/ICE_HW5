#3번, B835193 석채원
def isPrime(n):
    count = 0
    for i in range(2,n-1): #2부터 n-1로 나눈다, 1과 자기자신 제외
        if(n%i==0):
            count+=1
    if (count==0): # 나누어서 0이되는 수가 하나도 없다(1과 자기자신 제외):소수
        return True
    else:
        return False

def main():
    num = int(input("정수를 입력하시오:"))
    for i in range(2,num):
        if(isPrime(i)==True):
            print(i,end=' ')

main()
    
    
                
        
    