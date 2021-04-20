#4번_B735042_김대겸

# 사용자로부터 10진수를 입력받고 deci2bin(n)을 호출하는 main() 선언
def main():
    x = int(input("10진수: "))
    print(deci2bin(x))
# 10진수를 2진수 문자열로 변환하는 함수 deci2bin(n) 선언
def deci2bin(n):
    binary = ""
    while n > 0:
        remain = n % 2
        n = n // 2
        binary = str(remain) + binary
    return "0b" + binary
# main() 호출
main()
