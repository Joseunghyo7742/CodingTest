from collections import deque
def solution(bgn, trgt, wrds):
    wrds_len= len(wrds)
    wrd_len= len(bgn)
    
    # trgt이 wrds안에 있기는 한지 확인, 없다면 0 반환
    if(trgt not in wrds):
        return 0
    
    # 단어 변경 가능한지 체크하는 함수
    def isChangable(w,t):
        flag=False
        for i in range(wrd_len):
            if(flag and w[i]!=t[i]):
                # 두개 이상 다를 경우임
                return False
            elif(not flag and w[i]!=t[i]):
                flag=True
        return flag
        
                
    q= deque()
    check=[0]*wrds_len
    
    for i in range(wrds_len):
        if(isChangable(bgn,wrds[i])):
            q.append(i)
            check[i]+=1

    while(q):
        idx= q.popleft()
        curr_word= wrds[idx]
        print("curr_word",curr_word)
        print("q:",q)
        
        if(curr_word==trgt):
            print('idx',idx,'return check',check)
            return check[idx]
        
        for i in range(wrds_len):
            print("curr:",curr_word,"trg:",wrds[i],"change?",isChangable(curr_word,wrds[i]))
            if(isChangable(curr_word,wrds[i]) and not check[i]):
                q.append(i)
                check[i]=check[idx]+1
                
    return 0
    
    # bfs로 구현
        # 큐에 넣을 때 words의 인덱스넣기. 
        # check=[]에는 0으로 채워넣고, 방문을 체크한다. 
        # 이미 방문한곳이라면 넘기기, 방문안했다면 바꿀 수 있는 단어인지 확인, 
        # 바꾼다면 check에 +1
        # 만약 단어가 cog라면 이전 문자의 check에 +1하고 끝내기 
        
        
