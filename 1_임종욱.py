#1번 C111152 임종욱

def getGrade(score):
    cut = [90,80,70,60]
    grade = ['A','B','C','D']
    #반복문을 통해 학점을 결정한다
    for c in range(4):
        if score >= cut[c]:
            Grade = grade[c]
            break #점수가 학점 커트라인 이상이면 반복문을 빠져나간다
        #60점 미만이면F이다
    if score < 60:
        Grade = 'F'
     
    return Grade
        

def main():
 score = int(input("점수를 입력하세요: "))
 print("성적은", getGrade(score), "입니다")
 
 
main()