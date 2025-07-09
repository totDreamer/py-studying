from collections import defaultdict

def best_sender(messages, senders):
    count_of_word = defaultdict(int)
    for message, sender in zip(messages, senders):                                                                                                      
        count_of_word[sender] += len(message.split())
    return max(count_of_word, key=lambda x: (count_of_word.get(x), x))


messages = ['bu bu da', 'bu bu da', 'bu bu da', 'bu bu da', 'bu bu da', 'bu bu net']
senders = ['dima', 'anri', 'timur', 'timur', 'anri', 'dima']

print(best_sender(messages, senders))