def solution(exp):
    cand=2
    right_idx=[] # 확실한 식
    uk_idx=[] # 불확실한 식  
    result=[]
    # 10진법을 k 진법으로 
    def decimalToK(k,value):
        res = 0
        i = 1              
        while True:
            quo = value // k   # 몫
            mod = value % k    # 현재 k진수의 한 자리
            res += mod * i 
            if quo == 0:
                break
            value = quo        # 합을 갱신하며 다음 자리로
            i *= 10        # 십진 자리값 10배로
        return res
    
    def getPlusValue(k, a, b):
        di_a = (a // 10) * k + (a % 10)  # 두 자리 k진수 -> 10진수 값
        di_b = (b // 10) * k + (b % 10)
        s = di_a + di_b                   # 10진 합
        return decimalToK(k,s)
        
    # k진법일 때 a,b 뺄셈 계산 함수
    def getMinusValue(k,a,b):
        di_a=(a//10)*k + (a%10)
        di_b=(b//10)*k + (b%10)
        minus_di= di_a-di_b
        return decimalToK(k,minus_di)
    
    # 최소 진법의 범위 구하기
    for i in range(len(exp)):
        strs= list(exp[i].split())
        # 식 구분
        if(strs[-1]=="X"):
            uk_idx.append(i)
        else:
            right_idx.append(i)
        # 식뜯어보면서 최대 수 구하기
        for c in strs:
            if(c not in ["+","-","=","X"]):
                for n in c:
                    cand= max(cand, int(n)+1)
        
    # 맞는 식을 덧셈,뺄셈에 따라 검증하기-> 함수 값과 동일하지 않으면         
        # 가능한 진법은 연속되거나, 하나로 확정되거나.
    cand_arr= [ 0 if i<cand else 1 for i in range(10)] # n진법이 후보면 1
    for i in right_idx:
        tmpa,sign,tmpb,ignore,value= list(exp[i].split())
        a,b,value= int(tmpa),int(tmpb),int(value)
        for j in range(len(cand_arr)):
            if(cand_arr[j]): # 검사해야할 진법일 경우
                if(sign=="+"):
                    if(getPlusValue(j,a,b)!=value):
                        cand_arr[j]=0
                    continue
                else:
                    if(getMinusValue(j,a,b)!=value):
                        cand_arr[j]=0
                    continue
    
    for k in uk_idx:
        tmpa,sign,tmpb,ignore,x= list(exp[k].split())
        a,b= int(tmpa),int(tmpb)
        tmp=-1
        flag=True
        for j in range(len(cand_arr)):
            if(not flag): break
            if(cand_arr[j]): # 검사해야할 진법일 경우
                if(sign=="+"):
                    v=getPlusValue(j,a,b)
                    if(tmp==-1):
                        tmp=v
                    if(tmp!=-1 and tmp!=v):
                        result.append(f"{a} + {b} = ?")
                        flag=False
                        break
                else:
                    v= getMinusValue(j,a,b)
                    if(tmp==-1):
                        tmp=v
                    if(tmp!=-1 and tmp!=v):
                        result.append(f"{a} - {b} = ?")
                        flag=False
                        break
        if(flag):
            result.append(f"{a} {sign} {b} = {tmp}")
        
    print(result)
    return result
                        
                
        
        
    