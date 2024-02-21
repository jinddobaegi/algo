import sys
sys.stdin = open("4949.txt")
input = sys.stdin.readline

# 이거 틀렸음 왜 일까...
def checkline(line):
    stack = []
    if line == ".":
        return "yes"
    for i in line:
        if i in ["(","["]:
            if i == "(":
                stack.append(")")
            elif i == "[":
                stack.append("]")

        if i in [")","]"]:
            if stack and i != stack[-1]:
                return "no"
            elif stack and i == stack[-1]:
                stack.pop() 

    if stack:
        return "no"
    return "yes"


lines = []
while True:
    line = input().rstrip()
    if line == ".":
        break
    lines.append(line[:-1])

for line in lines:
    # print(line)
    if line[-1] != ".":
        # print("no")
        print(checkline(line))

    # 반례를 못찾겠음
    
    
