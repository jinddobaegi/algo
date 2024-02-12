import sys
sys.stdin = open("16508.txt")
# input = sys.stdin.readline

# 틀렸음
def min_cost(target, books):
    n = len(books)
    INF = float('inf')
    dp = [INF] * (1 << len(target))  
    dp[0] = 0  

    for book_cost, book_title in books:
        book_mask = 0
        for char in set(book_title):  
            for i, target_char in enumerate(target):
                if char == target_char:
                    book_mask |= 1 << i  

        for prev_mask in range(1 << len(target)):
            new_mask = prev_mask | book_mask
            dp[new_mask] = min(dp[new_mask], dp[prev_mask] + book_cost)

    if dp[-1] == INF:
        return -1
    return dp[-1]

target_word = input().strip()
n_books = int(input())
books = []
for _ in range(n_books):
    cost, title = input().split(maxsplit=1)
    books.append((int(cost), title))

print(min_cost(target_word, books))
