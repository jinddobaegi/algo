import sys
sys.stdin = open('input.txt')
def checking(i):
    # 1, 4를 넣고 시작했다 가정
    # [1, 4]는 table의 0번 인덱스 => 검사는 1번 인덱스 부터
    time_table = []
    time_table.append(table[i]) # 내가 검사할 기준점을 리스트에 담아줌

    for j in range(i+1, n):
        if time_table[-1][1] <= table[j][0]: # 현재 내가 검사하고 있는 시간대의 시작이 기준 시간대의 시작보다 크거나 같으면 => 바로 시작 가능
            time_table.append(table[j])
        # 시간을 줄일 만한 부분 => 만약 [4, 6] 을 넣었다면 [4, x]는 다 패스해야됨

    return len(time_table)

n = int(input())
table = [list(map(int, input().split())) for _ in range(n)]

# 회의가 겹치지 않으면서 회의실을 사용할 수 있는 회의의 최대 개수
table.sort(key=lambda x: (x[1], x[0]))

cnt = 1
end = table[0][1]
for i in range(1, n):
    if table[i][0] >= end:
        cnt += 1
        end = table[i][1]
        # print(table[i][0], end)
print(cnt)



