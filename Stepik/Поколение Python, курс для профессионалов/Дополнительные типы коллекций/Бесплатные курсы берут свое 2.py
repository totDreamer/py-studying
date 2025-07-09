from collections import Counter

def total_profit(books, count_of_buyers):
    count_of_books = Counter(books.split())
    profit = 0
    for _ in range(int(count_of_buyers)):
        book, price = input().split()
        if count_of_books[book] >= 1:
            profit += int(price)
            count_of_books[book] -= 1
    print(profit)

books = input()
n = input()
total_profit(books, n)