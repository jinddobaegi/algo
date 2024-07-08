# LCS(Longest Common Subsequence, 최장 공통 부분 수열) 문제는 두 수열이 주어졌을 때, 
# 모두의 부분 수열이 되는 수열 중 가장 긴 것을 찾는 문제이다.

# 예를 들어, ACAYKP와 CAPCAK의 LCS는 ACAK가 된다.

# 입력
# 첫째 줄과 둘째 둘에 두 문자열이 주어진다.
# 문자열은 알파벳 대문자로만 이루어져 있으며, 최대 1000글자로 이루어져 있다.

# 출력 
# 첫째 줄에 입력으로 주어진 두 문자열의 LCS의 길이를, 
# 둘째 줄에 LCS를 출력한다.
# LCS가 여러 가지인 경우에는 아무거나 출력하고, 
# LCS의 길이가 0인 경우에는 둘째 둘을 출력하지 않는다.

import sys
sys.stdin = open('week18/9252/9252.txt')
input = sys.stdin.readline

char_1 = input().strip()
char_2 = input().strip()


def lcs(char_1, char_2):
    N = len(char_1)
    M = len(char_2)
    dp = [[0] * (M + 1) for _ in range(N + 1)]

    for i in range(1, N + 1):
        for j in range(1, M + 1):
            if char_1[i - 1] == char_2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
    
    lcs_length = dp[N][M]
    print(lcs_length)
    
    lcs_str = []
    i, j = N, M
    while i > 0 and j > 0:
        if char_1[i - 1] == char_2[j - 1]:
            lcs_str.append(char_1[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1
    
    lcs_str.reverse()
    
    if lcs_length > 0:
        print(''.join(lcs_str))

lcs(char_1, char_2)



    