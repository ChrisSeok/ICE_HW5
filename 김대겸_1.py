# 1번_B735042_김대겸

# main함수 선언
def main():
    score = int(input("점수를 입력하세요: "))
    print("성적은", getGrade(score), "입니다")
# getGrade(score)함수 선언
def getGrade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"
# main()호출
main()