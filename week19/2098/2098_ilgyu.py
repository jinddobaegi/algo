import sys
sys.stdin = open('input.txt')

n = int(input())
cities = [list(map(int, input().split())) for _ in range(n)]

# n개의 비트 모두 켠다는 뜻 1111같은거
visited_all = (1 << n) - 1
INF = float('inf')
dp = [[None] * (1<<n) for _ in range(n)]
# 이러면 dp의 열이 2**n개만큼 만들어짐
# dp[0][15] = True
# 이진법표기 dp[0][0000] = 십진법표기 dp[0][0]
# dp[0][1111] = dp[0][15] 이런식
# print(1<<2) = 4 ==> 1에서 100 된거
# print(1<<3) = 8 ==> 1에서 1000
# for m in dp:
#     print(m)

# dp[i][2] = dp[i][0010(이진수)] = i도시에서 시작해서 0,2,3번도시 방문후 시작점으로 돌아온 거리
# 이진수에서 1로 체크된 1번도시는 이미 방문했음
def find_path(cur, visited): # cur는 현재 도시, visited는 현재까지 방문한 도시들 -> 0011 이면 0,1번 도시방문, 2, 3번은 아직 방문x
    if visited == visited_all: # 재귀연산을 통해 만들어진 visited가 1111 같이 모두 방문한 이진수가 되면
        return cities[cur][0] or INF# 모든도시 다 방문했으면 다시 시작점까지의 거리 반환하게

    # None이 아니면 이전 재귀에서 이미 해당 값이 계산됐다
    # 그러면 중복호출됐다는 거니까 값만 반환
    if dp[cur][visited] is not None:
        return dp[cur][visited]

    tmp = INF
    for city in range(n):
        if visited & (1 << city) == 0 and cities[cur][city] != 0:
            # print(f"현재위치: {cur}, 다음 위치: {city}, 현재까지 경로 {format(visited, f'0{n}b')}")
            tmp = min(tmp, find_path(city, visited | (1 << city)) + cities[cur][city])
            # find_path(city, visited | ( 1 << city)) 는 현재도시(cur)에서 city로 이동한후 , city도시를 방문한 상태에서 나머지 도시 ( visited | ( 1 << city)) 를 방문후
            # 시작점으로 돌아오는 최소비용
            # 그러니까 현재 내 위치를 cur에서 city로 옮겨주고 경로에 city를 추가해주는거  => city로 이동하는거니까 cities[cur][city] 값 더해주기

    # 만약 visited = 0001, cur = 0, city = 1이면  ( 현재 0도시에 있고 , 검사할 도시가 1 )
    # visited & ( 1 << 1 )은 0001 & 0010 => 0000
    # 이말은 1번 도시는 아직 방문 안했다는 뜻
    # cities[0][1] != 0 => 0번도시에서 1번도시로 가는 길이 있다
    # visited | (1 << city) 이건 0001 | ( 1 << 1 ) 이거랑 같고
    # 0001 | 0010 이 됨 => 0011 이러면 0번도시랑 1번 도시 방문

    # 정리하면 위 for문은
    # 현재 내가 있는 도시에서, 여태까지 방문한 도시 기록(visited)를 들고
    # 다음도시를 검사하는데 여기서
    # 1. 그 도시를 방문했는지 ( visited와 도시번호( 1<< city)를 &연산을 통해 검사 )
    # 2. 현재 위치(Cur)에서 해당 도시까지 길이 있는지 검사를 해서
    # 만약 둘다 만족하면 tmp (비용 ) 를 갱신해주는데
    # 내가 0-1-2-3 순서로 도시들을 방문한다고 가정했을 때


    dp[cur][visited] = tmp
    return tmp


print(find_path(0, 1 << 0))


#  0-1-2-3 번 순서로 방문한다고 했을 때 그럼 맨 마지막 재귀 들어가기직전에
# tmp = min(tmp , find_path(3, visited | (1 << 3)) + cities[2][3])
# 그러면 마지막 재귀인 find_path(3, 1111)이 함수는 cities[3][0]을 return
# 그러면 해당함수는 끝나고
# 여기까지 계산을 해보면
#  find_path(3, visited | (1 << 3)) = cities[3][0]이고
# 바로 직전 함수로 돌아와서
# tmp = min(tmp, cities[3][0] + cities[2][3])이 됨 => find_path(2, 0111)의 tmp값임
# 근데 이전 재귀함수를 생각해보면 현재 바로 위 값은 2번도시를 방문한ㅅ ㅣ점에서 계산한거고
# 1번도시를 방문한 시점에서 보면 => 이 함수는 find_path(1, 0011)
# tmp = min(tmp, find_path(2, visited | ( 1 << 2)) + cities[1][2])이거고
# find_path(2, visited | ( 1 << 2))이 값은 바로 위에서 구한
# tmp = min(tmp, cities[3][0] + cities[2][3])
# 다시 풀어서 쓰면
# 1번 도시방문하고, visited = 0011인 시점에서의 tmp를 계산해보면 find_path(1, 0011)
# tmp = min(tmp, min(tmp, cities[3][0] + cities[2][3]) + cities[1][2])
# 여기까지 보면 find_path(1, 0011)은 최종적으로
# dp[1][0011] 을 반환하는데 이 값의 의미는 1에서 시작해가지고 아직 방문 안한 2, 3을 거쳐 다시 시작점으로 돌아오는 최소거리를 뜻함
# 이 최소거리가 함수내에서 tmp이고 70줄에서 min제거하고 봐보면
# tmp = cities[3][0] + cities[2][3] + cities[1][2]
# 보면 1에서 2로, 2에서 3으로, 3에서 0으로 가는 비용을 더한 값을 나타냄