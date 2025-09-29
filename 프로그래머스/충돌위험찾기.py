def solution(points, routes):
    MAX_N= 101
    m= len(routes[0])
    result=0
    robots=len(routes)
    '''
    현재 로봇들의 위치를 담는 배열 loc [r,c]
    현재 로봇의 타겟 노드를 담는 배열 targ
    최종 노드들만 담은 last 
    만약 targ와 같은 노드라면 다음 타겟으로 설정바꾸기
    한타임이 지날 때마다 로봇의 현재 위치 배열에 중복노드가 있다면 result+=
    '''   
    
    last=[points[i[-1]-1] for i in routes] #최종 종착지 노드들
    curr=[points[i[0]-1] for i in routes] #현재 노드, 시작은 첫번째 경로
    dest=[points[i[1]-1] for i in routes] #다음 가야할 노드, 시작은 두번쨰 경로
    idx= [1]*robots # 다음 목적지 인덱스
    
    def enc(p):  # p: [r, c]
        return p[0] * MAX_N + p[1]

    while True:
        # --- 충돌 체크 ---
        seen = set()
        dup = False
        for i in range(robots):
            key = enc(curr[i])
            if key in seen:
                dup = True
                break
            seen.add(key)
        if dup:
            result += 1
        
        # 모든 로봇이 마지막 종착지에 도착했을 때 끝낸다.
        if(last == curr):
            break
    
        #로봇 각각 한칸씩 이동하기
        for i in range(robots):
            cr,cc= curr[i]
            nr,nc= dest[i]
            if cr != nr:
                curr[i][0] += 1 if nr > cr else -1
            elif cc != nc:
                curr[i][1] += 1 if nc > cc else -1
            
            # 목적지에 도달한 경우, 다음 목적지로 변경해준다.
            if(curr[i]==dest[i]):
                n_idx= idx[i]+1
                if(n_idx<m):
                    dest[i] = points[routes[i][n_idx] - 1]
                    idx[i]=n_idx
    return result    

    