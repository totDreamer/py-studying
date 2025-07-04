from collections import Counter

words_count = Counter(input().split(','))
longest_word = max(words_count, key=lambda x: len(x))

for word, count in sorted(words_count.items()):
  word_size = word + ' ' * (len(longest_word) - len(word))
  cost_of_word = sum(ord(c) for c in word if c != ' ')
  print(f'{word_size}: {cost_of_word} UC x {count} = {cost_of_word*count} UC')