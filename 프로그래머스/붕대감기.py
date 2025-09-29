def solution(bandage, health, attacks):
    hp= health #체력
    last_time= attacks[-1][0] #마지막 시간
    conti= 0 #연속초
    last_m= 0 #마지막 몬스터 인덱스
    time=0 #현재 시간
    
    contiTime,hpPerSec,bonusHp= bandage
    
    while(time<=last_time and hp>0):
        # 몬스터의 공격시간이라면 공격처리 and continue
        if(attacks[last_m][0]==time):
            conti=0# 연속성 0으로 초기화
            hp-= attacks[last_m][1]# 체력 깎기
            last_m+=1
            time+=1
            continue
        # 몬스터 공격시간 아닌 경우 
        elif(hp<=health):   
            time+=1
            hp=min(hp+hpPerSec, health)# 초당 체력 회복
            conti+=1
            if(conti==contiTime):# 연속성이 연속 시간과 같다면 추가 회복량
                conti=0
                hp=min(hp+bonusHp, health)
                
            
        
    if(hp<=0):
        return -1
    else:
        return hp
      
      
      