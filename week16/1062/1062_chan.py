import sys
sys.stdin = open("week16/1062/1062.txt")
input = sys.stdin.readline
from itertools import combinations

def readable(words, mask):
    count = 0
    for word in words:
        readable = True
        for char in set(word[4:-4]):  # 'anta'와 'tica'를 제외한 부분
            if not (mask & (1 << (ord(char) - ord('a')))):
                readable = False
                break
        if readable:
            count += 1
    return count

N, K = map(int, input().split()) # N: 단어의 수, K: 가르칠 글자 수
words = [list(input().strip()) for _ in range(N)] # 단어 입력
# print(words)
if K < 5:
    # 필수 글자 5개를 가르칠 수 없다면 단어를 읽을 수 없으므로 0 출력
    print(0)
else:
    # 필수 글자 'a', 'n', 't', 'i', 'c'를 포함하는 초기 비트마스크 설정
    basic_mask = 0
    for char in 'antic':
        basic_mask |= (1 << (ord(char) - ord('a')))
    
    # 단어에서 'a', 'n', 't', 'i', 'c'를 제외한 글자만 고려
    all_chars = set()
    for word in words:
        for char in set(word[4:-4]):
            if char not in 'antic':
                all_chars.add(char)

    all_chars = list(all_chars)

    if len(all_chars) <= (K - 5):
        # 모든 문자를 가르칠 수 있다면 모든 단어를 읽을 수 있음
        print(N)
    else:
        max_readable = 0
        # 모든 조합을 탐색하여 최대 읽을 수 있는 단어 수를 계산
        for comb in combinations(all_chars, K - 5):
            mask = basic_mask
            for char in comb:
                mask |= (1 << (ord(char) - ord('a')))
            max_readable = max(max_readable, readable(words, mask))
        
        print(max_readable)