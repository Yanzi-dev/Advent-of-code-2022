from collections import deque


def mix(mix_number: int, deck: deque):
    indexes = deque(range(0, len(deck)))
    length = len(indexes)
    for _ in range(mix_number):
        for index in range(length):
            position = indexes.index(index)
            for queue in [deck, indexes]:
                queue.rotate(position * -1)
                pop_left_value = queue.popleft()
                if queue == deck:
                    value = pop_left_value
                queue.rotate(value * -1)
                queue.appendleft(pop_left_value)
    zero = deck.index(0)
    grove = [deck[(zero + i * 1000) % (len(deck))] for i in range(1, 4)]
    print("star1" if mix_number == 1 else "star2", str(sum(grove)))


def main():
    print("Day 20 of lurk")
    handle = open("input.txt")
    datas_star1 = deque()
    datas_star2 = deque()
    for line in handle:
        datas_star1.append(int(line.strip()))
        datas_star2.append(811589153 * int(line.strip()))
    mix(1, datas_star1)
    mix(10, datas_star2)


main()
quit()
