from sys import stdin

input = stdin.readline

arr = list(list(map(int, input().split())) for _ in range(10))

'''
큰 색종이부터 체크하는 방식으로 풀었음
17%쯤에서 막힘
아래가 그 반례임

0 0 0 0 0 0 0 0 0 0
0 0 1 1 1 1 1 1 0 0
0 0 1 1 1 1 1 1 0 0
0 0 1 1 1 1 1 1 0 0
0 0 1 1 1 1 1 1 0 0
0 0 1 1 1 1 1 1 0 0
0 0 1 1 1 1 1 1 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
'''

# paper_dict = {
#     1: 5,
#     2: 5,
#     3: 5,
#     4: 5,
#     5: 5,
# }
#
#
# # n의 크기를 가진 색종이 체크
# def paper_check(r, c, n):
#     for y in range(n):
#         for x in range(n):
#             # 전체 배열을 돌면서 n*n의 1이 있는지 확인
#             if not (0 <= r+y < 10 and 0 <= c+x < 10 and arr[r+y][c+x]):
#                 return False  # 안되면 탈출
#
#     # 체크 다 되면 0으로 바꾸기
#     else:
#         for y in range(n):
#             for x in range(n):
#                 arr[r+y][c+x] = 0
#         return True
#
#
# # 큰 색종이부터 체크!
# paper_cnt = 0
# for k in range(5, 0, -1):
#     for i in range(10):
#         for j in range(10):
#             # 값이 1인지 / k*k의 색종이 남아있는지 / 확인하는 함수 결과가 True인지
#             if arr[i][j] and paper_dict[k] > 0 and paper_check(i, j, k):
#                 paper_dict[k] -= 1
#                 paper_cnt += 1
#
# cnt_ones = sum(map(sum, arr))  # 체크 후 1이 남아있는지 확인
#
# if cnt_ones:
#     print(-1)
# else:
#     print(paper_cnt)