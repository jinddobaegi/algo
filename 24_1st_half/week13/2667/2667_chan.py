import sys
sys.stdin = open("week13/2667/2667.txt")
input = sys.stdin.readline

def num_count(row, col):
    count = 0
    queue = [(row, col)]
    while queue:
        x, y = queue.pop()
        for dx, dy in delta:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0 and graph[nx][ny] == 1:
                visited[nx][ny] = 1
                count += 1
                queue.append((nx, ny))
    if count == 0:
        return 1 
    return count
    # 본 함수는 옆의것이 1일때 카운트를하기때문에 (1,1같은 경우에는 2를 리턴한다. 왜냐면 처음에 세지 않기 때문이다.) visited차이
    # 옆에것이 1이 아닐경우에는 한번을 세지 못한다 그렇기때문에 1을 리턴해준다.(함수호출조건자체가 1일 경우기 때문에 카운트해준다.)
    
    

N = int(input())
graph = [list(map(int, input().strip())) for _ in range(N)]
result = []

delta = [(0, 1), (0, -1), (1, 0), (-1, 0)]
visited = [[0] * N for _ in range(N)]

result = []
for row in range(N):
    for col in range(N):
        if graph[row][col] == 0:
            continue
        if graph[row][col] == 1 and visited[row][col] == 0:
            result.append(num_count(row, col))

print(len(result))
for i in sorted(result):
    print(i)
            

            
