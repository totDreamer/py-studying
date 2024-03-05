name = input()
print(f"Привет, {name.title()}, как твои дела?")

print(f"Привет, {name.lower()}")
print(f"Привет, {name.upper()}")
print(f"Привет, {name.title()}")


print("Invoker said: 'Education has the power'")


author_name = "Тимо"
message = f"Любимая фраза {author_name.title()} - 'Капитан {author_name.title()} на посту!'"
print(message)

error_name = "  аКаЛи  "
print(error_name)
print(error_name.rstrip().lower())
print(error_name.lstrip().upper())
print(error_name.strip().title())

print("Invoker said: \n\t'Education has the power'")