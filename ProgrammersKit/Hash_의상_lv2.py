from collections import Counter
def solution(clothes):
    answer=1
    classified_clothes = [row[1] for row in clothes] #각 행의 두 번째 행을 추출
    counter= Counter(classified_clothes) #classified clothes를 기준으로 Counte하여 딕셔너리로 출
    for i in counter.values():
        answer*=(i+1)
    answer-=1
    return answer


