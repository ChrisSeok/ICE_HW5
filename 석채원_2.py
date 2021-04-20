#2번, B835193 석채원
def getGCD(x,y):
    gcd = 0
    # i goes up from 1 to min(x,y)
    for i in range(1,min(x,y)+1):
    #if both x,y can be divided by i, i is the gcd
        if(x%i==0)and(y%i==0):
            gcd = i
    return gcd

    
def main():
 x = int(input("첫 번째 정수: "))
 y = int(input("두 번째 정수: "))
 print(getGCD(x,y))
main()
