from itertools import permutations

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

lst = []
for i in range(1, 9):
    lst.append(i)

max_score = 0
for i in permutations(lst):
    i = list(i)
    order = i[:3] + [0] + i[3:]

    player = 0
    score = 0
    for j in range(N):
        out = 0
        b1, b2, b3 = 0, 0, 0  # 베이스
        while out < 3:
            if arr[j][order[player]] == 0:
                out += 1
            elif arr[j][order[player]] == 1:
                score += b3
                b1, b2, b3 = 1, b1, b2
            elif arr[j][order[player]] == 2:
                score += b2 + b3
                b1, b2, b3 = 0, 1, b1
            elif arr[j][order[player]] == 3:
                score += b1 + b2 + b3
                b1, b2, b3 = 0, 0, 1
            elif arr[j][order[player]] == 4:
                score += b1 + b2 + b3 + 1
                b1, b2, b3 = 0, 0, 0

            player += 1
            if player == 9:
                player = 0

    max_score = max(max_score, score)

print(max_score)