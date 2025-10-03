

def solution(people, limit):
    people.sort(reverse=True)
    result=0
    s,e=0,len(people)-1
    while(s<=e):
        high= people[s]
        low= people[e]
        if(high+low<=limit): # 두사람이 탄 경우 
            s+=1
            e-=1
        else:
            s+=1
        result+=1
    return result
