import sys
sys.setrecursionlimit(10**6)

n,m = map(int, sys.stdin.readline().rstrip().split())

node = [[] for _ in range(n+1)] # 직원 n명의 직속상사 담는 리스트
sangsa = list(map(int, sys.stdin.readline().rstrip().split()))
compliment = [0 for _ in range(n+1)]

def dfs(num, sizeOfCompliment) :
    for k in node[num] :
        if k>num :
            #print(k, ":", compliment[k], "///",num ,":", compliment[num])
            compliment[k]+=sizeOfCompliment
            dfs(k, sizeOfCompliment)

for i in range(1,n+1) :
    node[i].append(sangsa[i-1])
    if sangsa[i-1]!=-1 : node[sangsa[i-1]].append(i)

for j in range(m) :
    i, w = map(int, sys.stdin.readline().rstrip().split())
    compliment[i]+= w
    dfs(i, w)

for i in compliment[1::] :
    print(i, end=" ")