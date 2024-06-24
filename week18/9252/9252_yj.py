import sys
input = sys.stdin.readline

S1 = [""] + list(input().strip())
S2 = [""] + list(input().strip())

len_1 = len(S1)
len_2 = len(S2)

LCS = [[""] * len_2 for _ in range(len_1)]

for i in range(1, len_1):
    for j in range(1, len_2):
        if S1[i] == S2[j]:
            LCS[i][j] = LCS[i-1][j-1] + S1[i]
        else:
            if len(LCS[i-1][j]) >= len(LCS[i][j-1]):
                LCS[i][j] = LCS[i - 1][j]
            else:
                LCS[i][j] = LCS[i][j - 1]

ans = LCS[-1][-1]
print(len(ans))
if len(ans) != 0:
    print(ans)