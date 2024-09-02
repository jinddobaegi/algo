import sys
from itertools import permutations
sys.stdin = open("week27/17281/17281.txt")
input = sys.stdin.readline

def cal(lineup, innings):
    score = 0
    number = 0

    for inning in innings:
        out = 0
        bases = [0,0,0]

        while out < 3:
            point = inning[lineup[number]-1]

            if point == 0: # 아웃
                out += 1
            elif point == 1: # 안타
                score += bases[2] #3루에 있는사람이 점수로 들어옴 
                bases = [1] + bases[:2] # 베이스를 새롭게 초기화
            elif point == 2: # 모든 주자가 2루씩 진루
                score += bases[1] + bases[2] #2루와 3루
                bases = [0,1] + bases[:1]
            elif point == 3:
                score += sum(bases)
                bases = [0,0,1]
            elif point == 4:
                score += sum(bases) + 1
                bases = [0,0,0]

            number = (number+1)%9 #이닝변경시 순번이동
    
    return score
 
N = int(input())
innings = [list(map(int, input().split())) for _ in range(N)] 

origin = [2, 3, 4, 5, 6, 7, 8, 9]
max_score = 0
for perm in permutations(origin):
    lineup = list(perm[:3]) + [1] + list(perm[3:])

    max_score = max(max_score, cal(lineup, innings))

print(max_score)

