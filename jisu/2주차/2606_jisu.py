C = int(input()) # 컴퓨터 수
N = int(input()) # 연결된 수

connections = [list(map(int, input().split())) for _ in range(N)]
virus = {1}
cnt = 0 # 연결된 컴퓨터 수

while True:
    for a, b in connections: # 연결된 애들 중에
        if (a or b) in virus: # virus 걸린 컴퓨터가 있다면
            virus.add(a) # set에 넣어주고
            virus.add(b) # 개별로 넣을 수 있으니 두 개 다 넣어줌
        cnt += 1 # 연결된 컴퓨터를 찾을 때마다 cnt 1씩 추가
    if cnt == N: # 연결된 컴퓨터를 다 찾으면 while문 멈춰
        break
answer = len(virus) - 1 # 바이러스 걸린 컴퓨터 수 - 1번 컴퓨터(1대)
print(answer)