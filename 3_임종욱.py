#3번  C111152 임종욱

#소수는 자신과 자기자신만 약수로 가진다
def isPrime(i):
    j = 1
    GCD = []
    while j <= i:
        if i % j == 0:
            GCD += [j]
        j += 1
        
    return GCD == [1,i] #결과로 true와 false를 반환한다
    
    
def main():
    n = int(input('정수 입력하시오: '))
    if n > 2:
        i = 1
        while i <= n:
            if isPrime(i):
                print(i,end=" ")
            i += 1

main()
        
    
