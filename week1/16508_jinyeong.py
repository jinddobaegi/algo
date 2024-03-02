# t = input()
# N = int(input())
#
# book_list = []  # 책의 리스트
# isUsed = list(0 for i in range(N))  # N번째 책이 쓰였는지 확인하기 위해 만든 리스트
# price_dict = dict()  # 책의 가격표
#
# for i in range(N):
#     p, b = input().split()
#     book_list.append(b)
#     price_dict[b] = p
#
# # 타겟 단어를 한 글자 씩 순회하면서 어디에 있는지 체크, cnt 올림
# # 최종적으로는 cnt가 0이 아닌 책의 가격만 확인
# # 모든 책의 cnt가 0이면 -1 출력
#
# for x in t:
#     for idx in range(N):
#         # idx번 책에 x라는 글자가 포함되어있으면
#         if x in book_list[idx]:
#             # cnt 늘려주고
#             isUsed[idx] += 1

# 포기
# https://blog.chanwookim.me/boj-16508-python-%EC%A0%84%EA%B3%B5%EC%B1%85.html
