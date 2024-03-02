''' 
idea
- 두 리스트를 정렬한다
- 1중 루프를 돌면서 비교한다. 
- 예외처리로 completion을 돌았는데 return이 없다면 participant의 마지막 주
'''
def solution(participant, completion):
    participant.sort()
    completion.sort()
    
    for i in range(len(completion)):
        if(participant[i]!=completion[i]):
            return(participant[i])
    
    return participant[len(participant)-1]
  
  #빠른 답
import collections
def solution(participant, completion):
	answer= collections.Counter(participant)- collections.Counter(completion)
	return list(answer.keys())[0]
'''
collections.Counter은 배열의 요소들과 해당 요소들의 개수를 세어 딕셔너리 형태로 반환함.
차집합 연산이 가능
'''
  