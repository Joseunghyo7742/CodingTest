MX= 1000005;
dat=[0]*MX #실제 데이터 저장
pre=[-1]*MX # 이전 노드 인덱스
nxt=[-1]*MX # 다음 노드 인덱스
unused=1 # 0번은 dummy head, 다음에 사용할 인덱스

# 노드 삽입함수
def insert(addr, num):
  # addr 위치 뒤에 num삽입
  dat[unused]=num
  pre[unused]= addr
  nxt[unused]= nxt[addr]
  
# 노드 삭제함수


# 순회하는 함수
