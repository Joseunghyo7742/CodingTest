#실패로 블로그 참고
#BFS 넓게 탐색 '+,-'부호에 따라 이진트리 형식으로 모든 경우의 수 작성
#모든 경우의 수 계산 후 target과 같은지 확인
def solution(numbers, target):
    leaves=[0]
    answer = 0
    
    for num in numbers:
        temp=[]
        for lef in leaves:
            temp.append(lef+num)
            temp.append(lef-num)
        leaves=temp
    
    for i in leaves:
        if(i==target):
            answer+=1
    return answer
