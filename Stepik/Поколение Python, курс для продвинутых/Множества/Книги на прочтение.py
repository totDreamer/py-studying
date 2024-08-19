n, m, k, x, y, z, t, a = int(input()), int(input()), int(input()), int(input()), int(input()), int(input()), int(input()), int(input())
n_m = n + m - x - t
m_k = m + k - y - t
k_n = k + n - z - t
only_one = k - m_k - k_n - t + m - m_k - n_m - t + n - n_m - k_n - t #Прочитали только одну книгу
only_two = n_m + m_k + k_n #Прочитали только 2 книги
print(only_one)
print(only_two)
print(a - only_one - only_two - t) #Не прочитали ни одной