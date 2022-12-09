def main():
    print("Day 09 Lurkers !")
    handle = open("input.txt")

    lines = list()
    for line in handle:
        lines.append(line.strip())

    # up down left right
    directions_udlr = {
        'U': (-1, 0),
        'D': (1, 0),
        'L': (0, -1),
        'R': (0, 1)
    }

    head = (0, 0)
    tail = [(0, 0) for i in range(9)]

    head_cases_touched = {tail[0]}
    all_cases_touched = {tail[8]}
    for line in lines:
        direction, steps_number = line.split()
        steps_number = int(steps_number)
        for step in range(steps_number):
            head = (head[0] + directions_udlr[direction][0], head[1] + directions_udlr[direction][1])
            tail[0] = move_tail(head, tail[0])
            for i in range(1, 9):
                tail[i] = move_tail(tail[i - 1], tail[i])
            head_cases_touched.add(tail[0])
            all_cases_touched.add(tail[8])
    print("star1", len(head_cases_touched))
    print("star2", len(all_cases_touched))


def move_tail(head, tail):
    head_x = head[0]
    head_y = head[1]
    tail_x = tail[0]
    tail_y = tail[1]
    distance_x = (head_x - tail_x)
    distance_y = (head_y - tail_y)
    if abs(distance_x) >= 2 and abs(distance_y) >= 2:
        tail = (head_x - 1 if tail_x < head_x else head_x + 1, head_y - 1 if tail_y < head_y else head_y + 1)
    elif abs(distance_y) >= 2:
        tail = (head_x, head_y - 1 if tail_y < head_y else head_y + 1)
    elif abs(distance_x) >= 2:
        tail = (head_x - 1 if tail_x < head_x else head_x + 1, head_y)
    return tail


main()
quit()
