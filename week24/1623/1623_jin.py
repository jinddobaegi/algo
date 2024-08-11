from sys import stdin, setrecursionlimit

setrecursionlimit(10 ** 6)
input = stdin.readline

# 1 == 사장
# seniors 값은 부모 노드
# juniors 값엔 자식 노드 리스트

N = int(input())
tempers = [0] + list(map(int, input().split()))  # N개 -> 사장 포함
seniors = [0, 0] + list(map(int, input().split()))  # N-1개 -> 사장 제외
juniors = [[] for _ in range(N + 1)]
for jun in range(2, N + 1):
    sen = seniors[jun]
    juniors[sen].append(jun)


# DP 활용
# DP[i][j]는 i번 사람을 루트로 하는 서브트리에서 i의 참석여부가 j(0 or 1)일 때의 날라리 기질 최댓값
# DP[1][0]과 DP[1][1] 값과 각 경우에 참석하는 사람 번호 구해보자


def solution(x):
    # 방문한 적 있으면 바로 DP값 반환
    if visited[x]:
        return DP[x]

    # 방문한 적 없으면 방문 표시
    visited[x] = 1

    # 말단 직원일 때
    if not juniors[x]:
        # 본인 참여 (미참여 => 어차피 0)
        DP[x][1] = tempers[x]
        members[x][1].append(x)
        return DP[x]

    # 말단 직원 아닐 때
    DP[x][1] += tempers[x]  # 참여할 때 내 날라리 값
    members[x][1].append(x)  # 멤버 갱신
    for jun in juniors[x]:
        jun_res = solution(jun)  # 각 부하의 DP 값

        # 내가 참여하는 경우
        DP[x][1] += jun_res[0]  # 부하직원 불참 시 DP 값
        members[x][1] += members[jun][0]

        # 내가 불참하는 경우
        # 부하직원 불참이 더 큰 경우
        if jun_res[0] > jun_res[1]:
            DP[x][0] += jun_res[0]
            members[x][0] += members[jun][0]

        # 부하직원 참가가 더 큰 경우
        else:
            DP[x][0] += jun_res[1]
            members[x][0] += members[jun][1]

    return DP[x]


BOSS = 1
DP = [[0, 0] for _ in range(N + 1)]  # 행: 0~N, 열: 0/1
members = [[[], []] for _ in range(N + 1)]  # 행: 0~N, 열: 0/1일 때 인원
visited = [0] * (N + 1)
boss_res = solution(BOSS)
boss_mems = members[BOSS]
print(boss_res[1], boss_res[0])
print(*(sorted(boss_mems[1]) + [-1]))
print(*(sorted(boss_mems[0]) + [-1]))