def solution(info, edges):
    n = len(info)

    # 1) 트리(유향): 부모 -> 자식들
    graph = [[] for _ in range(n)]
    for parent, child in edges:
        graph[parent].append(child)

    # 2) 상태: (현재까지 모은 양 수, 늑대 수, 방문 가능한 후보 노드들)
    #    - 후보 노드: 지금 "바로" 갈 수 있는 노드들(이미 방문해서 열린 자식들 포함)
    #    - 루트(0)는 문제 조건상 '양'이므로, 시작 양=1, 늑대=0, 후보는 0의 자식들
    answer = 0

    def dfs(current_sheep, current_wolf, candidate_nodes):
        """후보들 중 하나를 선택해서 방문 → 자식 추가 → 조건(양 > 늑대) 유지되면 계속 탐색"""
        nonlocal answer
        # 지금까지 모은 양의 최대값 갱신
        if current_sheep > answer:
            answer = current_sheep

        # 후보가 비어있어도 괜찮다: 더 이상 갈 곳이 없으면 여기서 끝
        # 후보가 있으면 각 후보를 하나씩 선택해 분기
        for next_node in list(candidate_nodes):   # 원본을 건드리지 않기 위해 복사본으로 순회
            # 다음 분기를 위한 후보 집합 만들기:
            #  - 방금 방문할 next_node는 후보에서 빼고
            #  - 그 노드의 자식들을 후보에 추가
            next_candidates = candidate_nodes.copy()
            next_candidates.remove(next_node)
            next_candidates.extend(graph[next_node])

            # next_node의 동물에 따라 수 변동
            if info[next_node] == 0:              # 양
                next_sheep = current_sheep + 1
                next_wolf  = current_wolf
                # 양 > 늑대 조건이 항상 참 → 바로 진행
                dfs(next_sheep, next_wolf, next_candidates)

            else:                                  # 늑대
                next_sheep = current_sheep
                next_wolf  = current_wolf + 1
                # 가지치기: 양이 늑대보다 많을 때만 진행
                if next_sheep > next_wolf:
                    dfs(next_sheep, next_wolf, next_candidates)
                # 아니면 이 분기는 중단

    # 시작 상태 구성
    # 루트(0)는 방문한다고 가정하고 양+1, 후보는 0의 자식들로 시작
    start_sheep = 1     # info[0] == 0 (항상 양)
    start_wolf  = 0
    start_candidates = graph[0][:]   # 0의 자식들(복사)

    dfs(start_sheep, start_wolf, start_candidates)
    return answer
