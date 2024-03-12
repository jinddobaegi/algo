import sys
sys.stdin = open('input.txt')

def Binary_Search_Upper(data_list, x):
    # bottom = [1, 3, 5] 넣은 경우
    # left, right는 인덱스
    left = 0
    right = len(data_list) - 1
    while left <= right:
        mid = (left + right) // 2
        if data_list[mid] <= x:
            left = mid + 1
        else:
            right = mid - 1
    return len(data_list) - (right + 1)

N, H = map(int, input().split()) # (2 ≤ N ≤ 200,000, 2 ≤ H ≤ 500,000) N은 짝수
stick = []
for _ in range(N):
    stick.append(int(input()))
# print(stick)
top = []
bottom = []

for i in range(N):
    if i % 2 == 0:
        bottom.append(stick[i])
    else:
        top.append(stick[i])

# 여기까지 하고 top, bottom을 크기순으로 정렬?
top.sort()
bottom.sort()
print(top)
print(bottom)

ans = N                         #장애물의 최솟값
cnt = 0                         #구간 몇 개 있는지
for h in range(1, H + 1):
    down_num = Binary_Search_Upper(bottom, h - 1)
    up_num = Binary_Search_Upper(top, H - h)
    cur_num = down_num + up_num     #현재 mid 값을 기준으로 잘랐을 때의 장애물의 수
    if cur_num < ans:               #새로운 최솟값이 나오면 정답 업데이트; 개수는 1부터 다시 셈
        ans = cur_num
        cnt = 1
    elif cur_num == ans:            #현재 최솟값과 같은 값이 한 번 더 나오면 개수 1 증가
        cnt += 1
print(ans, cnt)




