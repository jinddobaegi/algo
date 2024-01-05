'''
input
3
6
7 2 5 3 4 6
6
3 1 4 16 23 12
8
18 57 11 52 14 45 63 40

output
[2, 3, 5, 7, 4, 6]
[1, 3, 4, 16, 23, 12]
[11, 14, 18, 40, 52, 45, 63, 57]
'''


import heapq as hq

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    num_list = list(map(int, input().split()))

    # method_1)

    # my_heap = []

    # for num in num_list:
    #     hq.heappush(my_heap, num)
    # print(my_heap)

    # res = 0
    # while N - 1 > 0:
    #     N //= 2
    #     res += my_heap[N - 1]


    # method_2)

    my_heap = [0] * (N+1)
    last_idx = 1
    for num in num_list:
        # 마지막 삽입 위치가 0이면, 즉 비어있으면
        if not my_heap[last_idx]:
            my_heap[last_idx] = num
        # 마지막 삽입 위치가 0이 아니면, 즉 값이 이미 있으면
        else:
            # 일단 삽입
            last_idx += 1
            my_heap[last_idx] = num
            # 후 우선 순위 고려 및 교체
            # 부모와 비교, 삽입한 값이 더 작으면 교체
            parent = last_idx // 2
            child = last_idx
            # 삽입한 값이 작은 동안 while문 도는 것
            while my_heap[child] < my_heap[parent]:
                my_heap[child], my_heap[parent] = my_heap[parent], my_heap[child]
                child = parent
                parent //= 2

    res = 0
    while N > 0:
        N //= 2
        res += my_heap[N]



    print(f'#{tc} {res}')

