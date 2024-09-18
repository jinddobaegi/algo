from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)
input = stdin.readline

# C개의 공유기를 집들에 설치할 것임
# 공유기를 설치했을 때 가장 인접한 공유기 간 거리를 최대로 해야 함

N, C = map(int, input().split())
homes = list(int(input()) for _ in range(N))
homes.sort()

# 블로그 참고ㅜ
# 이분탐색을 쓰는데, 어떤 지점을 찾는 게 아닌
# 공유기 사이의 거리를 찾는 데에 이분탐색을 쓴다?

s = 1  # 공유기 간 최소 거리
e = homes[N-1] - homes[0]  # 공유기 간 최대 거리
res = 0  # update할 공유기 간 최소 거리

while s <= e:
    m = (s+e)//2  # 현재 설정한 공유기 간 거리
    cur = homes[0]  # 0번째 집에 설치하고 시작
    cnt = 1  # 설치 공유기 대수
    
    # 현재 거리가 m일 때
    for i in range(1, N):
        # 공유기를 돌면서, 이전 공유기부터 정해놓은 거리 이상?
        if homes[i] >= cur + m:
            # 설치
            cnt += 1
            cur = homes[i]

    # 가능한 수보다 적게 설치?
    if cnt < C:
        # 공유기 간 거리를 줄여야 함
        e = m-1
    # 가능한 수 이상으로 설치?
    else:
        # 저장하고, 공유기 간 거리 늘려보자
        res = m
        s = m+1

print(res)

# 실패 코드
# # 그럼 지하철에서 자리 앉는 것처럼 이분 탐색 써서
# # 양 끝에 먼저 설치
# # 중간값 가까운 데에 설치
# # 그 둘 사이 설치, 이런 식으로 가보자
#
#
# def bin_search(l, r):
#     home_l, home_r = homes[l], homes[r]
#     t = (home_r + home_l) // 2
#     while l <= r:
#         m = (l + r) // 2
#         if homes[m] == t:
#             return m
#         elif homes[m] > t:
#             r = m-1
#         else:
#             l = m+1
#     
#     tmp1 = homes[l-1] - home_l
#     tmp2 = home_r - homes[l]
#     if tmp1 > tmp2:
#         return l-1
#     else:
#         return l
#
#
# # 우선순위 큐 만들 거임, 원소는 (-거리, 집1, 집2)
# # 거리가 가장 먼 두 점 사이마다 공유기를 설치할 것임
# # 공유기 한 개를 설치하면, 우선순위 큐에
# # (-거리1, 집1, 새집), (-거리2, 새집, 집2) 이렇게 두 개를 넣을 거임
# 
# pq = []
# min_v = homes[N-1] - homes[0]
# heappush(pq, (-min_v, 0, N-1))
# while C > 2 and pq:
#     d, li, ri = heappop(pq)
#     mi = bin_search(li, ri)
#     if mi in (li, ri):
#         continue
#     d1 = homes[mi]- homes[li]
#     d2 = homes[ri] - homes[mi]
#     min_v = min(min_v, d1, d2)
#     heappush(pq, (-d1, li, mi))
#     heappush(pq, (-d2, mi, ri))
#     C -= 1
# 
# print(min_v)