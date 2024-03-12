import sys
sys.stdin = open("1158.txt")
from collections import deque

# 요세푸스 제거되는순서
# 1234567 = 3
# 456712 = 6
# 71245 = 2
# 4571 = 7
# 145 = 5
# 141 = 1
# 4 = 4



num, count = map(int, input().split())
list = deque()
result = []
for i in range(1, num+1): # 번호순서대로 추가하기
    list.append(i)
for _ in range(num): 
    if len(list) > count-1: # 3일경우에.... 2초과일 경우 순번-1 만큼의 앞의 수를 뒤로 옮기고 순번이오면 result에 추가
        for _ in range(count - 1):
            list.append(list.popleft())
        result.append(list.popleft())
    else: # count-1 만큼일 경우에는 순번대로 추가해준다. 원형이기때문에
        while list:
            for _ in range(count-1):
                list.append(list.popleft())
            result.append(list.popleft())

print("<",end="")
print(", ".join(map(str, result)),end="")
print(">")



