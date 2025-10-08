def solution(video_len, pos, op_start, op_end, commands):
    # 초로 바꿔주는 함수
    def getSeconds(strT):
        m,s= map(int,strT.split(":"))
        return m*60+s
        
    # 현재 위치가 오프닝 위치면 op_end로 보내는 함수
    def IsInOpening(t):
        if(ops<=t<=ope):
            return True
        else:
            return False
            
    ops= getSeconds(op_start)
    ope= getSeconds(op_end)
    full= getSeconds(video_len)
    cur_t= getSeconds(pos)
    
    
    for c in commands:
        if(IsInOpening(cur_t)):
            cur_t= ope
        if(c=="prev"):
            cur_t= max(0, cur_t-10)
        else:
            cur_t= min(full,cur_t+10)
        
    if(IsInOpening(cur_t)):
        cur_t=ope
    
    
    # 출력시 값형태 되돌리기
    m= cur_t//60
    s= cur_t%60
    return f"{m:02d}:{s:02d}"
