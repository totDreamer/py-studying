messages = ["hello", "help", "ok", "no", "yes"]
sent_messages = []

def send_messages(*, messages : list):
    while messages:
        message = messages.pop()
        sent_messages.append(message)
        print(message.title())




send_messages(messages=messages[:])
print(f"'messages' list - {messages}\n'sent_messages' - {sent_messages}")