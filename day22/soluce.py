data = open("input.txt").read()
lines = [x for x in data.split('\n')]

grid, instructions = data.split('\n\n')
grid = grid.split('\n')
instructions = instructions.strip()

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
zones = [(0, 1), (0, 2), (1, 1), (2, 1), (2, 0), (3, 0)]

width = len(grid)
height = len(grid[0])

for x in range(width):
    while len(grid[x]) < height:
        grid[x] += ' '


def main_star1():
    x = y = i = 0
    direction = 1
    while grid[x][y] != '.':
        y += 1

    while i < len(instructions):
        n = 0
        while i < len(instructions) and instructions[i].isdigit():
            n = n * 10 + int(instructions[i])
            i += 1
        for _ in range(n):
            xx = (x + directions[direction][0]) % width
            yy = (y + directions[direction][1]) % height
            if grid[xx][yy] == ' ':
                x = (x + directions[direction][0]) % width
                y = (y + directions[direction][1]) % height
                while grid[x][y] == ' ':
                    x = (x + directions[direction][0]) % width
                    y = (y + directions[direction][1]) % height
                if grid[x][y] == '#':
                    break
                (x, y, direction) = (x, y, direction)
                continue
            elif grid[xx][yy] == '#':
                break
            else:
                x = xx
                y = yy
        if i == len(instructions):
            break
        turn = instructions[i]
        if turn == 'L':
            direction = (direction + 3) % 4
        elif turn == 'R':
            direction = (direction + 1) % 4
        i += 1
    directions_score = {0: 3, 1: 0, 2: 1, 3: 2}
    return (x + 1) * 1000 + (y + 1) * 4 + directions_score[direction]


edge_len = height // 3


def get_land(x, y):
    for i, (xx, yy) in enumerate(zones):
        if xx * edge_len <= x < (xx + 1) * edge_len and yy * edge_len <= y < (yy + 1) * edge_len:
            return i + 1, x - xx * edge_len, y - yy * edge_len


def compute_coords(xx, yy, direct, new_direct):
    global x
    if direct == 0:
        x = yy
    if direct == 1:
        x = xx
    if direct == 2:
        x = edge_len - 1 - yy
    if direct == 3:
        x = edge_len - 1 - xx

    if new_direct == 0:
        return edge_len - 1, x
    if new_direct == 1:
        return x, 0
    if new_direct == 2:
        return 0, edge_len - 1 - x
    if new_direct == 3:
        return edge_len - 1 - x, edge_len - 1


def main_star2():
    x = y = i = 0
    direction = 1
    while grid[x][y] != '.':
        y += 1

    while i < len(instructions):
        n = 0
        while i < len(instructions) and instructions[i].isdigit():
            n = n * 10 + int(instructions[i])
            i += 1
        for _ in range(n):
            xx = (x + directions[direction][0]) % width
            yy = (y + directions[direction][1]) % height
            if grid[xx][yy] == ' ':
                land, xx, yy = get_land(x, y)
                new_land, new_direction = {
                    (1, 0): (6, 1), (1, 1): (2, 1), (1, 2): (3, 2), (1, 3): (5, 1),
                    (2, 0): (6, 0), (2, 1): (4, 3), (2, 2): (3, 3), (2, 3): (1, 3),
                    (3, 0): (1, 0), (3, 1): (2, 0), (3, 2): (4, 2), (3, 3): (5, 2),
                    (4, 0): (3, 0), (4, 1): (2, 3), (4, 2): (6, 3), (4, 3): (5, 3),
                    (5, 0): (3, 1), (5, 1): (4, 1), (5, 2): (6, 2), (5, 3): (1, 1),
                    (6, 0): (5, 0), (6, 1): (4, 0), (6, 2): (2, 2), (6, 3): (1, 2)
                }[(land, direction)]

                nx, ny = compute_coords(xx, yy, direction, new_direction)
                xx, yy = zones[new_land - 1]
                nx, ny = xx * edge_len + nx, yy * edge_len + ny

                if grid[nx][ny] == '#':
                    break
                (x, y, direction) = (nx, ny, new_direction)
                continue
            elif grid[xx][yy] == '#':
                break
            else:
                x = xx
                y = yy
        if i == len(instructions):
            break
        turn = instructions[i]
        if turn == 'L':
            direction = (direction + 3) % 4
        elif turn == 'R':
            direction = (direction + 1) % 4

        i += 1
    directions_score = {0: 3, 1: 0, 2: 1, 3: 2}
    return (x + 1) * 1000 + (y + 1) * 4 + directions_score[direction]


print("Day 22 of lurk")
print("star1", main_star1())
print("star2", main_star2())
quit()
