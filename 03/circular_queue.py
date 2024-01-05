# circular queue

# 선형큐와 다르게 front와 rear를 0으로 초기화함
# 공백상태와 포화상태를 구분하기 위해서
# front가 있는 자리는 빈 자리로 두기 위해서!

# 공백상태: rear == front
# 포화상태: (rear+1) & Qsize == front

# rear는 계속 1씩 추가하는 반면,
# front는 갱신할 때마다 Qsize를 넘지 않도록 갱신해줌

# Qsize보다 한 칸 적게 사용함

def enqueue(data):
    global rear
    global front
    # 삽입 전에 포화상태인지 고려해줘야 함
    # 포화상태일 때
    if (rear+1) % q_size == front:
        # front에서 하나 방출
        front = (front + 1) % q_size
    rear = (rear+1) % q_size
    cQ[rear] = data


def dequeue():
    global front
    if rear == front:
        print('queue is empty')
    else:
        front = (front+1) % q_size

        return cQ[front]


q_size = 4
cQ = [0] * q_size
front = rear = 0

enqueue(1)
enqueue(2)
enqueue(3)
enqueue(4)
enqueue(5)

print(cQ)
print(f'front: {front}, rear: {rear}')

print(dequeue())
print(dequeue())
print(dequeue())
print(f'front: {front}, rear: {rear}')