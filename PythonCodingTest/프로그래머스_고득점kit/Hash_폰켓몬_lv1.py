###[내 풀이]
#오답: sort(nums)가 아닌 nums.sort() /length(nums) 가 아닌 len(nums)
def solution(nums):
    nums.sort() #nums 오름차순 정렬
    answer = 1 #일단 최소 하나니까 1을 디폴트값으로 함
    
    for i in range(1,len(nums)):  
        if(len(nums)/2 =<answer): #폰켓몬 고르는 수 초과하면 반복문 끝내기
            break
        else:
            if(nums[i]==nums[i-1]): #중복된 종류면 카운트하지 않음
                continue
            else: #중복되지 않으면 카운
                answer+=1
    return answer
  
  ###[남 풀이]
def solution(ls):
	return min(len(ls)/2, len(set(ls)))

'''
[Set 함수]
- 수학에서 집합
- 중복을 삭제
- set([1,1,3,2]) => 리스트를 셋으로 변환해 중복값 삭제 후 셋 반환 {1,3,2}
- test.add() , test.update)[,,] - 요소 추가
- test.remove() -요소 집합에서 제거 , 없을 경우 에러보냄 
- test.pop() - 집합에서 요소 제거 후 리턴
https://docs.python.org/ko/3/library/stdtypes.html?highlight=set#set-types-set-frozenset
'''