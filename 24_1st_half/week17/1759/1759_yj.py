# 암호는 최소 한 개의 모음과 최소 두 개의 자음으로 구성 & 알파벳이 증가하는 순서로 배열
from itertools import combinations

L, C = map(int, input().split())  # 암호 길이, 문자 종류
alphabet = input().split()
alphabet.sort() # 증가하는 순서여야 하므로 정렬시킴

# 암호의 조건에 맞는지 확인
def is_valid(password):
    vowel_cnt = 0
    cnt = 0
    for i in password:
        if i in "aeiou":
            vowel_cnt += 1
        else:
            cnt += 1
    return vowel_cnt >= 1 and cnt >= 2

combination = combinations(alphabet, L)

for password in combination:
    if is_valid(password):
        print("".join(password))