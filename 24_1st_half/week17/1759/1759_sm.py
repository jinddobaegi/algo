# 암호만들기
# 골드 5
'''
1. 최소 모음 1개 + 최소 자음 2개
2. 증가하는 순으로 배치
'''


import sys
input = sys.stdin.readline

# 입력값 읽기: l (암호 길이)와 c (사용 가능한 문자 개수)
l, c = map(int, input().split())

# 사용 가능한 문자들을 읽고 사전 순으로 정렬
alpha = list(input().split())
alpha.sort()

# 현재 암호 조합 저장
result = []

# 문자가 모음인지 확인
def checking(alpha):
    if alpha == 'a' or alpha == 'e' or alpha == 'i' or alpha == 'o' or alpha == 'u':
        return 0  # 모음이면 0 반환
    return 1  # 자음이면 1 반환

# 현재 암호 조합 출력
def _print():
    for a in result:
        print(a, end='')
    print()





def dfs(depth, idx, check_1, check_2):
    # 기본 조건: 현재 조합의 길이가 원하는 암호 길이와 같으면
    if depth == l:
        # 모음이 최소 1개 이상이고 자음이 최소 2개 이상인지 확인
        if check_1 >= 1 and check_2 >= 2:
            _print()  # 조건을 만족하면 조합을 출력
        return

    # 현재 인덱스부터 사용 가능한 문자들에 대해 반복
    for i in range(idx, c):
        check = checking(alpha[i])  # 현재 문자가 모음인지 자음인지 확인

        # 자음인 경우 자음 개수 증가
        if check:
            check_2 += 1
        # 모음인 경우 모음 개수 증가
        else:
            check_1 += 1

        # 현재 문자를 결과 리스트에 추가
        result.append(alpha[i])
        # 개수랑 인덱스 업데이트
        dfs(depth+1, i+1, check_1, check_2)
        # 마지막에 추가한 문자 제거
        result.pop()

        # 제거한 문자에 따라서 모음자음 개수 줄이기
        if check:
            check_2 -= 1
        else:
            check_1 -= 1

# 초기 값으로 깊이 우선 탐색 시작
dfs(0, 0, 0, 0)

