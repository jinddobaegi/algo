T = input()
N = int(input())
price = []
books = []
min_cost = 100000000000
for i in range(N):
    p, m = input().split()
    price.append(int(p))
    books.append(m)

def wordinbook(word, book, price):
    cnt = 0
    for w in word:
        if w in book:
            cnt += 1
            book = book.replace(w, ' ', 1) # 제일 첫번째로 발견한 일치하는 글자는 공백으로 대체해주기.
            if cnt == len(word):
                return price
    return min_cost

result = []
for i in range(1 << N):
    word = ""
    cost = 0
    for j in range(N): # 여기서부터
        if (i & 1 << j) != 0:
            word += books[j]
            cost += price[j] # 여기까지 다시 고민해보기

    result.append(wordinbook(T, word, cost))

result = min(result) # 모든 조합에서의 결과를 찾아서 그 중 제일 적은 값을 결과로
if result == min_cost:
    result = -1

print(result)