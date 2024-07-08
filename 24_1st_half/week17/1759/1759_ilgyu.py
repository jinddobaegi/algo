import sys
sys.stdin = open('input.txt')
from itertools import combinations

L, C = map(int, input().split()) # (3 ≤ L ≤ C ≤ 15)
alpha = list(map(str, input().split()))
alpha.sort()
# print(alpha)
# 최소 한개의 모음, 최소 두개의 자음
# 알파벳은 오름차순

# 주어진 c개의 알파벳들 중 L개로 이루어진 조합을 구하는데
# 여기에 모음은 최소 1개, 자음은 2개 이상 포함되어야 하고
# 이 조합은 오름차순
# my_list = ['b', 'f', 'z', 'a']
# my_list.sort()
# print(my_list)

vowels = ['a', 'e', 'i', 'o', 'u']

x = combinations(alpha, L)
for case in x:
    vowel_cnt = 0 # 모음 수
    consonants_cnt = 0 # 자음 수
    for char in case:
        if char in vowels:
            vowel_cnt += 1
        else:
            consonants_cnt += 1
    if vowel_cnt >= 1 and consonants_cnt >= 2:
        print(''.join(case))


