import sys
sys.stdin = open('1931.txt')

def check():
    global count
    for i in checktime2:
        # print(i)
        # print(checktime)
        if i:
            print(i)
            for start, end in i:
                # print(start, end)
                if all(checktime[start:end+1]) == 0: #여기부분이 잘됬는지 확인 필요
                    # print(checktime[start:end+1])
                    count += 1
                    # print(count)
                    for j in range(start, end):
                        checktime[j] = 1
                else:
                    continue
total = int(input())
checktime = [0]*(24+1)
checktime2 = [[]for _ in range(24)]
timelist = []
count = 0

for _ in range(total):
    a, b = map(int, input().split())
    timelist.append((a,b))

for start, end in timelist:
    checktime2[end - start].append([start, end])

check()

print(count)

# 틀림
