import sys
sys.stdin = open('1931.txt')

def check():
    global count
    for i in checktime2:
        # print(i)
        # print(checktime)
        if i:
            # print(i)
            for start, end in i:
                # print(start, end)
                overlap = any(checktime[start:end+1])  # 겹치는 시간이 있는지 확인
                if not overlap:
                    count += 1
                    for j in range(start, end):
                        checktime[j] = 1
                    #     print('숫자를 알아보자 몇이냐',j)
                    # print('start,end = ',start, end)
                    # print(checktime, 'checktime++++++++')
                elif any(checktime[start:end+1]) == 1:
                    # print('틀린거 start,end = ',start, end)
                    # print('틀린거 체크',all(checktime[start:end+1]) == 0)
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

# import sys
# sys.stdin = open('1931.txt')

# def check():
#     global count
#     for i in checktime2:
#         # print(i)
#         # print(checktime)
#         if i:
#             print(i)
#             for start, end in i:
#                 # print(start, end)
#                 if all(checktime[start:end+1]) == 0: # start부터 end까지 0이면 True
#                     # print(checktime[start:end+1])
#                     count += 1
#                     # print(count)
#                     # print(all(checktime[start:end+1]) == 0)
#                     for j in range(start, end+1):
#                         checktime[j] = 1
#                     #     print('숫자를 알아보자 몇이냐',j)
#                     # print('start,end = ',start, end)
#                     # print(checktime, 'checktime++++++++')
#                 elif any(checktime[start:end+1]) == 1:
#                     # print('틀린거 start,end = ',start, end)
#                     # print('틀린거 체크',all(checktime[start:end+1]) == 0)
#                     continue
# total = int(input())
# checktime = [0]*(24+1)
# checktime2 = [[]for _ in range(24)]
# timelist = []
# count = 0

# for _ in range(total):
#     a, b = map(int, input().split())
#     timelist.append((a,b))

# for start, end in timelist:
#     checktime2[end - start].append([start, end])

# check()

# print(count)

# # 틀림

