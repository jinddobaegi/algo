
# 문제
# 영선회사에는 매우 좋은 문화가 있는데, 바로 상사가 직속 부하를 칭찬하면 그 부하가 부하의 직속 부하를 연쇄적으로 칭찬하는 내리 칭찬이 있다.
#  즉, 상사가 한 직속 부하를 칭찬하면 그 부하의 모든 부하들이 칭찬을 받는다.
# 모든 칭찬에는 칭찬의 정도를 의미하는 수치가 있는데, 이 수치 또한 부하들에게 똑같이 칭찬 받는다.
# 직속 상사와 직속 부하관계에 대해 주어지고, 칭찬에 대한 정보가 주어질 때, 각자 얼마의 칭찬을 받았는지 출력하시오,

# 입력
# 첫째 줄에는 회사의 직원 수 n명, 최초의 칭찬의 횟수 m이 주어진다. 직원은 1번부터 n번까지 번호가 매겨져 있다. (2 ≤ n, m ≤ 100,000)
# 둘째 줄에는 직원 n명의 직속 상사의 번호가 주어진다. 직속 상사의 번호는 자신의 번호보다 작으며, 최종적으로 1번이 사장이다. 1번의 경우,
#  상사가 없으므로 -1이 입력된다.
# 다음 m줄에는 직속 상사로부터 칭찬을 받은 직원 번호 i, 칭찬의 수치 w가 주어진다. (2 ≤ i ≤ n, 1 ≤ w ≤ 1,000)
# 사장은 상사가 없으므로 칭찬을 받지 않는다.

# 출력
# 1번부터 n번의 직원까지 칭찬을 받은 정도를 출력하시오.

# 예제 입력 1 
# 5 3 직원수 칭찬횟수
# -1 1 2 3 4 직원번호 직속상사번호 -1 사장 1 부하 2 부하 3 부하 4 부하
# 2 2 직원번호 칭찬의 수치
# 3 4 직원번호 칭찬의 수치
# 5 6 직원번호 칭찬의 수치
# 예제 출력 1 
# 0 2 6 6 12

import sys
sys.stdin = open("14267.txt")
input = sys.stdin.readline

n, m = map(int, input().split()) # 직원수, 칭찬횟수
boss = list(map(int, input().split())) # 직원번호, 직속상사번호 4의 상사는 3 3의 상사는 2 2의 상사는 1 1의 상사는 -1
ch = [0] * n # 직원수 만큼 0으로 초기화
for _ in range(m): # 칭찬의 횟수
    a, b = map(int, input().split()) # 직원번호, 칭찬의 수치
    ch[a - 1] += b # 해당직원의 -1이 직속상사 칭찬의 수치를 더해줌
for i in range(n): # 직원수만큼 반복 왜? 칭찬의 수치를 더해줘야 하기 때문
    if boss[i] != -1: # 직속상사가 -1이 아니면
        ch[i] += ch[boss[i] - 1] # 직원번호의 칭찬의 수치에 직속상사의 칭찬의 수치를 더해줌
print(*ch) 


