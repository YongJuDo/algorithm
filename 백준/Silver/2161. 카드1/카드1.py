N = int(input())
queue = list(range(1, N + 1))
discard_cards = []

while len(queue) > 1:
    discard_cards.append(queue.pop(0))
    queue.append(queue.pop(0))

print(*discard_cards, *queue)