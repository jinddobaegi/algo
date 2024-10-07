import sys
sys.stdin = open('input.txt')

n, k = map(int, input().split())
h = list(map(int, input().split()))

# print(h)

# 중간에 선을 그어서 나누는거임 숫자섞기 x

ans = [0] * (n-1)

for i in range(n-1):
    ans[i] = h[i+1] - h[i]

# print(ans) # 2, 2, 1, 4
# 여기서 1 ( 5와 6의 차이)은 둘 사이의 대각선을 없앨 경우 비용
ans.sort()
# k개의 집단으로 나누는 건 ans에서 n-k개의 구분선을 선택하는 것
# print(ans[:n-k]) # n-k 이전값까지
print(sum(ans[:n-k]))
