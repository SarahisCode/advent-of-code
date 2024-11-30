scratchcards = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11""".strip().split("\n")
_sum = 0
to_process = {}
for i in range(1, len(scratchcards)+1):
    to_process[i] = 1

for card in scratchcards:
    card_number = int(card.strip().split(": ")[0].split(" ")[-1])
    num_copies = to_process[card_number]
    _sum += num_copies
    to_use = card.strip().split(": ")[1]
    winning = to_use.split(" | ")[0].split(" ")
    have = to_use.split(" | ")[1].split(" ")
    matching = 0
    for num in have:
        if num in winning and num != "":
            matching += 1
    for i in range(card_number+1, card_number+1+matching):
        to_process[i] += num_copies
print(_sum)
