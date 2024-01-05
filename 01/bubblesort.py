arr = [1,5,2,63,6,27,88,23,11]

# 버블 소트
# 앞에서부터 자리를 교환해나가는 방식
# 한 바퀴가 끝나면 가장 큰 수가 맨 뒤로 가도록

N = len(arr)

for i in range(N-1, 0, -1):
    for j in range(i):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]

print(arr)