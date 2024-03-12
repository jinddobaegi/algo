import sys
sys.stdin = open("3986.txt")


def checkword(word):
    stack = []
    for i in word:
        if stack:
            if stack[-1] == "A" and i == "A":
                stack.pop()
            elif stack[-1] == "B" and i == "B":
                stack.pop()
        else:
            stack.append(i)
    if stack:
        return "no"
    return "ok"

N = int(input())
res = []
for _ in range(N):
    word = input()
    res.append(checkword(word))
print(res.count("ok"))
    
# 밑에는 맞는걸로 나오는데 위에는 틀린걸로 나옴 이유를 모르겠음!!
# def checkword(word):
#     stack = []
#     for i in word:
#         if stack and ((stack[-1] == "A" and i == "A") or (stack[-1] == "B" and i == "B")):
#             stack.pop()
#         else:
#             stack.append(i)
#     if stack:
#         return "no"
#     else:
#         return "ok"

# N = int(input())
# res = []
# for _ in range(N):
#     word = input()
#     res.append(checkword(word))
# print(res.count("ok"))


    