# 오아시스의 재결합
import sys
input= sys.stdin.readline

n= int(input()) #줄에 선 사람 수
stack=[999999]


cnt=0
# for _ in range(n):
#   k= int(input())
#   cnt+= len(stack)-1
#   (stack[-1]<=k):
#     stack.pop()
#   stack.append(k)

print(cnt)
# 출력: 서로 볼 수 있는 쌍의 수
# 바로 근접해있거나, 중간에 키 큰 사람이 없거나

# 5 2 2 4 4 5
# 10쌍

# 5 2 +1
# 5 2 2 +2
# 5 2 2 4 => 예외 발생. 2를 그냥 빼버림. 
# 


# 들어가기 전에 스택에 있는 길이만큼 더해준다.
# top보다 작으면 그냥 넣는다
# top보다 클 때까지 pop

