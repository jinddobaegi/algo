# from itertools import combinations
#
# def get_minimum_cost(T, books):
#     # 각 전공책에서 필요한 문자의 개수를 세는 함수
#     def counting(T, book):
#         count = {}
#         for letter in T:
#             count[letter] = book.count(letter)
#         return count
#
#     min_cost = 10000000000
#     for i in range(1, len(books) + 1):  # 전공책 -> 개수별 부분집합 생성
#         for subset in combinations(books, i):
#             # 부분집합에서 필요한 모든 문자를 포함하는지 확인
#             remaining_letters = [T.count(letter) for letter in T] # 필요한 문자의 개수
#             for price, book in subset:
#                 book_count = counting(T, book)
#                 remaining_letters = [max(0, remaining_letters[i] - book_count[letter]) for i, letter in enumerate(T)]
#                 if any(remaining_letters):
#                     break
#             else:
#                 # 부분집합에서 필요한 문자를 모두 포함하고 있는 경우
#                 min_cost = min(min_cost, sum(price for price, _ in subset))
#
#     return min_cost if min_cost != 10000000000 else -1
#
# # 입력 받기
# T = input()
# num_books = int(input())
#
# books = []
# for _ in range(num_books):
#     price, book = input().split()
#     books.append((int(price), book))
#
# # 결과 출력
# print(get_minimum_cost(T, books))

T = 'A'
remaining_letters = [T.count(letter) for letter in T]
