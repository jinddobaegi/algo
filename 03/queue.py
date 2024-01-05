# using deque

from collections import deque

q = deque()
q.append(1)
q.append(2)
q.append(3)
q.append(4)

pop1 = q.popleft()  # LIFO
pop2 = q.popleft()

q.append(5)
q.append(6)

print(pop1, pop2)
print(q)

