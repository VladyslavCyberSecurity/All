cards = {
    "Shylodupenko": 20,
    "Korychnyvenko": 10,
    "Daryna": 12000000
}

def pay_by_card(card_id):
    if card_id not in cards:
        return "Card doesn't exist"

    if cards[card_id] < 15:
        return "No money"
    else:
        cards[card_id] -= 15
        return "Paid"

print(pay_by_card("Daryna"))
