n, m = map(int, input().split())

# 인접 리스트 생성
rel = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    rel[a].append(b)
    rel[b].append(a)

# 결과 변수
result = 0

def main():
    global result
    # 각 노드를 시작점으로 관계 탐색
    for i in range(n):
        visited = [False] * n
        visited[i] = True
        if findFriends(i, 1, visited):  
            result = 1
            break


def findFriends(node, depth, visited):
    # 깊이가 5 이상이면 성공 조건을 만족
    if depth == 5:
        return True

    for friend in rel[node]:
        if not visited[friend]:
            visited[friend] = True
            #친구 관계가 안이어지면 다른 곳에서 이어질 수도 있기때문에 방문을 취소해야함. 
            if findFriends(friend, depth + 1, visited):
                return True
            visited[friend] = False

    return False

# 메인 함수 실행
main()
print(result)
