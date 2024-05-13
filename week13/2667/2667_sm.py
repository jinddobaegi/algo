# 실버1
# 단지번호 붙이기

# 그림 1>과 같이 정사각형 모양의 지도가 있다.
# 1은 집이 있는 곳을, 0은 집이 없는 곳을 나타낸다.
# 철수는 이 지도를 가지고 연결된 집의 모임인 단지를 정의하고, 단지에 번호를 붙이려 한다.
# 여기서 연결되었다는 것은 어떤 집이 좌우, 혹은 아래위로 다른 집이 있는 경우를 말한다.
# 대각선상에 집이 있는 경우는 연결된 것이 아니다. <그림 2>는 <그림 1>을 단지별로 번호를 붙인 것이다.
# 지도를 입력하여 단지수를 출력하고, 각 단지에 속하는 집의 수를 오름차순으로 정렬하여 출력하는 프로그램을 작성하시오.


# 그냥 dfs 로 하는게 나을듯


N = int(input())
graph = [list(map(int, input())) for _ in range(N)]
lst = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x, y):
    if x < 0 or x >= N or y < 0 or y >= N:
        return False

    if graph[x][y] == 1:
        global count
        count += 1
        graph[x][y] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx, ny)
        return True
    return False


count = 0
result = 0

for i in range(N):
    for j in range(N):
        if dfs(i, j) == True:
            lst.append(count)
            result += 1
            count = 0

lst.sort()  #내림차순정렬 때려주고
print(result)
for i in range(len(lst)):
    print(lst[i])