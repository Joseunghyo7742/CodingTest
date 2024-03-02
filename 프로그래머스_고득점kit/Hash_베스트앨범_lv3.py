def solution(genres, plays):
    answer = []
    temp=[]
    genre_order={}
    temp= [[genres[i], plays[i],i] for i in range(len(genres))]
    temp= sorted(temp, key= lambda x: (x[0], -x[1], x[2]))

    for i in temp:
      if i[0] not in genre_order: #딕셔너리형이니까 key값으로 있는지 확인
        genre_order[i[0]]=i[1] #해당 키값이 없으면 플레이횟수를 value로 담아줌
      else:
        genre_order[i[0]] += i[1]
    genre_order=sorted(genre_order.items(), key=lambda x: -x[1]) #items는 key와 value의 쌍을 튜플로 묶은 값으로 돌려준다. 딕셔너리는 순서가 없으니까

    for i in genre_order:
      count=0
      for j in temp:
        if(i[0]==j[0]): #같은 장르라면
          count+=1
          if(count>2):
            break
          else:
            answer.append(j[2]) #인덱스추가
                        
    return answer

print("solution1",solution(["classic", "pop", "classic", "classic", "pop"],[500, 600, 150, 800, 2500]))