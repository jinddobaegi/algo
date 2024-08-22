from sys import stdin

input = stdin.readline

N = int(input())
arr = list(map(int, input().split()))
S = int(input())
done = []


def solution(s):
    while s > 0 and arr != sorted(arr, reverse=True):
        # 앞으로 옮겨진 자리 확정 숫자들 제외하고
        # 앞에서부터 S+1개 중 가장 큰 수를 맨 앞으로
        d = len(done)
        e = min(d+S+1, N)
        tmp = arr[d:e]
        try:
            x = max(tmp)
        except:
            return
        x_idx = tmp.index(x) + d
        while s > 0 and x_idx != d:
            if arr[x_idx-1] < arr[x_idx]:
                arr[x_idx-1], arr[x_idx] = arr[x_idx], arr[x_idx-1]
                x_idx -= 1
                s -= 1
        done.append(x)


solution(S)
print(*arr)