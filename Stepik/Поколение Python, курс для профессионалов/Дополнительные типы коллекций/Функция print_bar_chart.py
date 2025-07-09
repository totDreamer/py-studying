from collections import Counter

def print_bar_chart(data, mark):
    counter = Counter(data)
    max_length = len(max(counter, key=lambda x: len(x)))
    for ob, count in sorted(counter.items(), key=lambda x: -x[1]):
        print(f'{ob + ' '*(max_length - len(ob)) } |{mark*count}')

print_bar_chart('beegeek', '+')

languages = ['java', 'java', 'python', 'C++', 'assembler', 'java', 'C++', 'C', 'pascal', 'C++', 'pascal', 'java']
print_bar_chart(languages, '#')