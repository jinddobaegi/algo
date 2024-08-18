# 신년 파티
# 뭘 이용해야할지도 모르겠음

N = int(input())
funny = [0] + [map(int, input().split())] # 날라리 기질
parents = [0, 0] + [map(int, input().split())] # (idx번호)직원의 직속상관
children = [[] for _ in range(N + 1)]

for child in range(2, N + 1): # 후배 리스트도 만들어주기
    idx = parents[child]
    children[idx].append(child)
