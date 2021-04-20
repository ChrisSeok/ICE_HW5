#5번, B835193 석채원
def getSorted(num1,num2):
    if(num1<num2):
        sorted = '('+str(num1)+','+str(num2)+')'
    else:
        sorted = '('+str(num1)+','+str(num2)+')'
    # 괄호와 쉼표 출력 위해 문자열로 반환 
    return sorted
    

def main():
 x = int(input("첫 번째 정수: "))
 y = int(input("두 번째 정수: "))
 print(getSorted(x, y))
 
main()
