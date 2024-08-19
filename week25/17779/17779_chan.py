import sys
sys.stdin = open("week25/17779/17779.txt")
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

def cal(si,sj,d1,d2):
    v = [[0]*N for _ in range(N)]
    alst = [0]*5

    v[si][sj] = 1
    j1 = j2 =sj
    for di in range(1, d1+d2+1):
        if di<=d1:  j1 -= 1
        else:       j1 += 1

        if di<= d2: j2 += 1
        else:       j2 -= 1
        v[si+di][j1:j2+1]=[1]*(j2-j1+1)
    
    for i in range(N):
        for j in range(N):
            if v[i][j]==1:  alst[4] += arr[i][j]
            else:
                if i<si+d1 and j<=sj:       alst[0]+=arr[i][j]
                if i<=si+d2 and sj<j:       alst[1]+=arr[i][j]
                if si+d1<=i and j<sj-d1+d2: alst[2]+=arr[i][j]
                if si+d2<i and sj-d1+d2<=j: alst[3]+=arr[i][j]

    return max(alst)-min(alst)

tot = sum(map(sum, arr))
ans = 100*N*N
for si in range(N-2):
    for sj in range(1, N-1):
        for d1 in range(1, N):
            if 0<=si+d1<N and 0<=sj-d1<N:
                for d2 in range(1, N):
                    if 0<=si+d1+d2<N and 0<=sj+d2<N:
                        ans=min(ans, cal(si,sj,d1,d2))

print(ans)