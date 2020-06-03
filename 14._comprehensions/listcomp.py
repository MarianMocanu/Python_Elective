l = []

for i in range(1, 10):
    l.append(i)

[i for i in range(1, 10)]

a = [chr(i) for i in range(65, 91) if i not in [70, 75, 80, 85]]
b = [chr(i) for i in range(65, 91) if i not in range(70, 80, 2)]

clothes_colors = ["Black", "White"]
sizes = ["s", "m", "l", "xl"]

sold_out = [("Black", "m"), ("White", "s")]
c = [(clothes_colors[i], sizes[j]) for i in range(2) for j in range(4) if (clothes_colors[i], sizes[j]) not in sold_out]

d = [(c, s) for c in clothes_colors for s in sizes if (c, s) not in sold_out]


signs = {'♠', '♡', '♢', '♣'}
numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
deck = {key: set(numbers) for key in signs}
deckList = [(x, y) for x in signs for y in numbers]
