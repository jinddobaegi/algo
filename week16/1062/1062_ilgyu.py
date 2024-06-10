# import sys
# sys.stdin = open('input.txt')
# from itertools import combinations
#
# N, K = map(int, input().split())
# words = [list(map(str, input())) for _ in range(N)]
#
# # print(words)
# # K는 가르치는 글자의 수
# # 학생들은 k개의 글자로만 이루어진 단어만을 읽을 수 있다
# # a n t a / t i  c a
# # a, n, t, i, c 이거 5개는 무조건 포함
# # 예제 1에서
# # antahellotica => x
# # antacartica => 기존 a n t i c 에서 r 추가로 가르침 ( k = 6 됨) => 읽기 o
#
# # 예제 2
# # k = 3
# # 아무것도 못 읽음
#
# # 기본적으로 k >= 5 이어야함
# # 그러니까 케이스를
# # k >= 5인 경우랑 아닌경우로 나눠서
#
# # if K < 5:
# #     print('0')
# # else:
#
# #
# # 1. 내가 가르칠 수 있는 글자수를 지정( K-5 )
# # 2. 글자들을 검사하면서 하나씩 까
# # 3. 만약 가르칠 수 있는 글자수가 0이 되면 ans를 프린트
#
# can_teach_words = K - 5
# # print(teach_words)
#
# # 1. 단어 리스트에서 K -5 개의 조합을 만듦
# # 2. 각각의 조합을 돌면서 basic에 단어의스펠링이 있는지 검사
# # 3. 만약 한 단어를 끝까지 돌았다면 ans + 1 해주고
# # 4. ans와 max_cnt를 비교
#
# pos = combinations(words, K - 5)
# # print(pos)
# max_ans = 0 # 최종정답
# for combi in pos:
#     # print(combi)
#     ans = 0
#     basic = ['a', 'c', 'i', 'n', 't']
#     cnt = K-5 # 하나의 조합에서 기본글자 외에 추가로 가르칠 수 있는 스펠링 수
#     for word in combi:
#         for i in range(len(word)):
#             if word[i] not in basic and cnt > 0:
#                 cnt -= 1
#                 basic.append(word[i])
#             if i == len(word) - 1:
#                 ans += 1
#     max_ans = max(ans, max_ans)
#
# if can_teach_words < 0:
#     print(0)
# else:
#     print(max_ans)






# 2트

# import sys
# sys.stdin = open('input.txt')
# from itertools import combinations
#
# N, K = map(int, input().split())
# words = [list(map(str, input())) for _ in range(N)]
# # print(words)
#
# basic = ['a', 'c', 'i', 'n', 't'] # 기본 단어
# can_teach = K - 5 # 가르칠 수 있는 값 - 기본 단어 수
#
# if can_teach < 0:
#     print(0)
#
# else:
#     my_words = []
#
#     # 알파벳 리스트 a~z
#     a = [chr(i) for i in range(ord('a'), ord('z') + 1)]
#     additional_alphabet = [i for i in a if i not in basic] # a~z에서 basic 뺀 거
#
#
#     for word in words:
#         my_words.append(word[4:-4]) # 중간 부분 단어만 추출
#     print(my_words)
#     # print(additional_alphabet)
#
#     # 1. basic외에 K - 5 개를 추가로 가르치는 조합을 구하기
#     my_case = combinations(additional_alphabet, can_teach)
#
#     # 2. 각각 조합의 케이스에 따라 my_words를 검사
#     max_cnt = 0
#     for case in my_case:
#         # print(case)
#         # ['b']
#         my_basic = ['a', 'c', 'i', 'n', 't']
#         cnt = 0
#
#         # 기본 스펠링에 각 조합의 추가 알파벳 넣어주기
#         for char in case:
#             my_basic.append(char)
#
#         # 입력 단어들을 돌면서
#         # 중복값 처리
#         for my_word in my_words:
#             for i in range(len(my_word)):
#                 if my_word[i] not in my_basic:
#                     continue
#                 if i == len(my_word) - 1:
#                     cnt += 1
#
#         max_cnt = max(cnt, max_cnt)
#     print(max_cnt)
# 파이썬 시간초과 / 파이파이 틀렸습니다

# 3트 접근방식 바꾸기
# list 대신 set이용 (중복되는 애들이 많으니까)
import sys
sys.stdin = open('input.txt')
from itertools import combinations

N, K = map(int, input().split())
words = [list(map(str, input())) for _ in range(N)]
# print(words)

basic = {'a', 'c', 'i', 'n', 't'} # 기본단어를 set에 저장
can_teach = K - 5 # 가르칠 수 있는 값 - 기본 단어 수

if K < 5:
    print(0)
    exit()

additional_alphabet = set() # 추가로 배워야할 알파벳들 담을 set
my_words = [] # 조합만들고 검사하기 위해서 중간에 있는 단어만 담는 리스트
              # 얘를 list로 한 이유는 set으로 만들면 중복된 단어들이 없어져버려서 제대로 검사가 안됨

# 단어에서 기본 단어를 제외한 나머지 알파벳을 추출
for word in words:
    center_chars = set(word) - basic
    additional_alphabet.update(center_chars)
    my_words.append(center_chars)

additional_alphabet = list(additional_alphabet)
# print(additional_alphabet)
# print(my_words)

# 이 조건문 안넣으면 자꾸 64퍼에서 실패함
# k가 커서 모든 단어를 가르칠 수 있는 경우 불필요한 계산 안하게 하려는 조건 
if can_teach >= len(additional_alphabet):
    print(N)
    sys.exit()

max_cnt = 0
# print('additional:', additional_alphabet)

# 추가 알파벳 중에서 can_teach개를 뽑는 모든 조합에 대해
for case in combinations(additional_alphabet, can_teach):
    total = basic.union(case) # union => set끼리 합침
    cnt = 0
    # 1번 예제의 경우 can_teach값은 1 => 1개의 알파벳을 추가로 배울 수 있음
    # 만약 case 가 'e' 인경우 total = {'a', 'c', 'i', 'n', 't', 'e'} => 즉 이게 현재 내가 아는 단어
    # 이 for문에서는 이 total을 가지고 입력 단어들을 검사함

    # 모든 단어를 검사하여 읽을 수 있는 단어의 개수를 셈
    for word in my_words:
        if word.issubset(total): # a.issubset(b) => a가 b의 하위집합 즉 포함되는지 확인
            cnt += 1

    max_cnt = max(max_cnt, cnt)

print(max_cnt)

