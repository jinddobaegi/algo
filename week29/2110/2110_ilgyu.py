import sys
sys.stdin = open('input.txt')

n, c = map(int, input().split())
home = []
for _ in range(n):
    a = int(input())
    home.append(a)
home.sort()

# start, end는 공유기 사이의 최소, 최대거리
start, end = 1, home[n-1] - home[0]
ans = 0
while start <= end:
    mid = (start + end) // 2
    current = home[0]
    cnt = 1 # 현재 설치한 공유기의 수
    # 여기까지 봤을 때 맨 첨에 첫 번쨰 집에 공유기를 설치하고 시작

    for i in range(1, len(home)):
        # 이 for문에서 home[i]는 다음 공유기의 위치
        if home[i] >= current + mid:
            cnt += 1
            current = home[i]

    if cnt >= c:
        start = mid + 1
        ans = mid
    else:
        end = mid - 1
print(ans)

