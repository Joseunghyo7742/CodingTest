import math
def solution(prgs, spds):
    # prgs- 배포되어야 하는 순서대로 적힌 작업 진도
    # spds- 작업 개발 속도
    # 앞 기능 배포될때 함께 배포됨
    
    '''
    1. 배포 가능 일 구하기
    2. 스택0 보다 큰게 나오면 스택을 모두 비우기 
    [5,10,1,1,20,1]
    
    '''
    
    answer = []
    takes=[]
    length=len(prgs)
    
    for i in range(length):
        t= math.ceil((100-prgs[i])/spds[i])
        takes.append(t)
    
    stack=[takes[0]]
    for t in range(1,length):
        next=takes[t]
        
        if(next<=stack[0]):
            stack.append(next)
        else:
            answer.append(len(stack))
            stack.clear()
            stack.append(next)
    if(stack):
        answer.append(len(stack))
    
    return answer
        
    

    
    return answer