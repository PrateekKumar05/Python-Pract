def verify_card_number(card_number):
    card_number = card_number.replace(" ", "").replace("-", "")

    total = 0
    reverse_digits = card_number[::-1]

    for i in range(len(reverse_digits)):
        digit = int(reverse_digits[i])

        if i % 2 == 1:
            digit *= 2
            if digit > 9:
                digit -= 9

        total += digit

    if total % 10 == 0:
        return "VALID!"
    else:
        return "INVALID!"