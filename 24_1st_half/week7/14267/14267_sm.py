# 회사문화1
# 골드4

# 메모리 초과난 코드.. (진짜 한참 기다리다 메모리 초과)
import sys
sys.setrecursionlimit(10**6)
n,m = map(int, input().rstrip().split())
senior = list(map(int, input().rstrip().split()))
# 직원 n명의 직속상사 담는 리스트
node = [[] for _ in range(n+1)]
compliment = [0 for _ in range(n+1)]

def dfs(n) : # 내 직속부하들도 점수주기
    for k in node[n] :
            # 내 칭찬 +
            compliment[k]+=compliment[n]
            dfs(k)

for i in range(1,n+1) :
    if senior[i-1]!=-1 :
        # 각 상사의 부하 담아
        node[senior[i-1]].append(i)

# 사람 i을 먼저 더하고  dfs를 돌려야지

for j in range(m) : # 먼저 각 사람이 받은 칭찬 저장 후
    getcompliment, w = map(int, input().rstrip().split())
    compliment[getcompliment] += w

# 사장님부터 검사 ㄱ
dfs(1)

# 인덱스1부터 긑까지)
compliment = compliment[1::]

for i in compliment:
    print(i, end=" ")