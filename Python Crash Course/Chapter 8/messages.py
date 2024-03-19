messages = ["hello", "help", "ok", "no", "yes"]


def show_messages(*, messages : list):
    for message in messages:
        print(message.title())


show_messages(messages=messages)