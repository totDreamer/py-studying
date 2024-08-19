n, m, k, x, y, z, t, a = (int(input()) for _ in range(8))

# Количество учеников, прочитавших только одну книгу
only_n = n - (x - m) - (z - k) + t
only_m = m - (x - n) - (y - k) + t
only_k = k - (z - n) - (y - m) + t

one_book = only_n + only_m + only_k

# Количество учеников, прочитавших только две книги
# Здесь (x + y + z) - 2 * t - (n + m + k) даст количество учеников, прочитавших только две книги
two_books = (x + y + z - 2 * t) - (n + m + k) + 3 * t

# Количество учеников, которые не прочитали ни одной книги
no_books = a - (n + m + k - (x + y + z - 2 * t))

print(one_book)
print(two_books)
print(no_books)
