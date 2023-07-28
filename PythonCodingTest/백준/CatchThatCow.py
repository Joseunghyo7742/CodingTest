from collections import deque
n,k= map(int,input().split())

if k<= n:
  print(n-k) #소가 농부보다 뒤에 있는 경우

else:
  queue= deque()
  queue.append((n,0)) #농부위치, 카운트
  visited= set([n])
  while True:
    current, cnt= queue.popleft()
    if current==k:
      print(cnt)
      break
    else:
      cnt+=1
      if current-1 not in visited:
        queue.append((current-1,cnt))
        visited.add(current-1)
        print("current-1:",current-1,"cnt:",cnt)
      if current < k:
        if current+1 not in visited:
          queue.append((current+1,cnt))
          visited.add(current+1)
          print("current+1:",current+1,"cnt:",cnt)
        if current*2 not in visited:
          queue.append((2*current, cnt))
          visited.add(current*2)
          print("current*2:",current*2,"cnt:",cnt)