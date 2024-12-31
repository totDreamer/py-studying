def hide_card(card_number):
    card_number = card_number.replace(' ', '')
    return '*' * 12 + card_number[-4:]