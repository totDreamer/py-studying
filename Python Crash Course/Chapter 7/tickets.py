flag = True
while flag:
    check_age = int(input("Write your age and I will show you the ticket price\n\t"))
    if check_age <= 3:
        print("Free entry for you")
    elif check_age <= 12:
        print("Ticket price $12")
    else:
        print("Ticket price $15")
    more = input("Do you need another ticket? Write 'yes' or 'no'\n\t")
    if more == "no":
        break