from collections import Counter

print("Day 23 of lurk")
datas = set()
with open("input.txt", "r") as f:
    for i, line in enumerate(f.readlines()):
        for j, char in enumerate(line.strip()):
            if char == '#':
                datas.add((i, j))

orientations = ((-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1))
directions = [(((-1, 0), (-1, 1), (-1, -1)), (-1, 0)),
              (((1, 0), (1, 1), (1, -1)), (1, 0)),
              (((0, -1), (-1, -1), (1, -1)), (0, -1)),
              (((0, 1), (-1, 1), (1, 1)), (0, 1))]

for round in range(10):
    proposed_destinations = {}
    for elf_position in datas:
        if not any((elf_position[0] + c[0], elf_position[1] + c[1]) in datas for c in orientations):
            continue
        for it in range(4):
            check_directions, proposed_direction, = directions[(round + it) % 4]
            if not any((d[0] + elf_position[0], d[1] + elf_position[1]) in datas for d in check_directions):
                proposed_destinations[elf_position] = (
                    elf_position[0] + proposed_direction[0], elf_position[1] + proposed_direction[1])
    proposed_destinations_counter = Counter(proposed_destinations.values())
    for elf_position, proposed_destination in proposed_destinations.items():
        if proposed_destinations_counter[proposed_destination] == 1:
            datas.remove(elf_position)
            datas.add(proposed_destination)

for elf in datas:
    min_i, max_i = elf[0], elf[0]
    min_j, max_j = elf[1], elf[1]
    break
for elf in datas:
    min_i, max_i = min(min_i, elf[0]), max(max_i, elf[0])
    min_j, max_j = min(min_j, elf[1]), max(max_j, elf[1])

height = max_i - min_i + 1
width = max_j - min_j + 1
empty_spaces = width * height - len(datas)
print("star1", empty_spaces)

datas = set()
with open("input.txt", "r") as f:
    for i, line in enumerate(f.readlines()):
        for j, char in enumerate(line.strip()):
            if char == '#':
                datas.add((i, j))

num_moved = 1
round = 0
while num_moved:
    proposed_destinations = {}
    for elf_position in datas:
        if not any((elf_position[0] + orientation[0], elf_position[1] + orientation[1]) in datas for orientation in orientations):
            continue
        for it in range(4):
            check_directions, proposed_direction, = directions[(round + it) % 4]
            if not any((d[0] + elf_position[0], d[1] + elf_position[1]) in datas for d in check_directions):
                proposed_destinations[elf_position] = (
                    elf_position[0] + proposed_direction[0], elf_position[1] + proposed_direction[1])
                break
    num_moved = 0
    proposed_destinations_counter = Counter(proposed_destinations.values())
    for elf_position, proposed_destination in proposed_destinations.items():
        if proposed_destinations_counter[proposed_destination] == 1:
            datas.remove(elf_position)
            datas.add(proposed_destination)
            num_moved += 1
    round += 1

print("star2", round)
