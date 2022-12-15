import re


def main():
    print("Day 15")
    row_number = 2000000
    not_present_position = set()
    handle = open("input.txt")
    circles = list()
    for line in handle:
        sx, sy, bx, by = (int(i) for i in re.findall(r'-?\d+', line))
        radius = abs(bx-sx) + abs(by-sy)
        circles.append((sx, sy, radius))
        distance = abs(row_number - sy)
        step_left = radius - distance

        if step_left < 0:
            continue

        for x in range(sx - step_left, sx + step_left +1):
            pos = (x, row_number)
            if pos != (bx, by):
                not_present_position.add(pos)
    print("star 1", len(not_present_position))

    for x, y, r in circles:
        for px, py, in get_boundary(x, y, r+1):
            if 0 <= px <= 4000000 and 0 <= py <= 4000000:
                for dx, dy, dr in circles:
                    if (abs(px-dx) + abs(py-dy)) <= dr:
                        break
                else:
                    print("star2 frequency", 4000000 * px + py)
                    break


def get_boundary(x, y, r):
    pos_extended = (x, y+r)
    while pos_extended != (x+r, y):
        pos_extended = (pos_extended[0]+1, pos_extended[1]-1)
        yield pos_extended
    while pos_extended != (x, y-r):
        pos_extended = (pos_extended[0]-1, pos_extended[1]-1)
        yield pos_extended
    while pos_extended != (x-r, y):
        pos_extended = (pos_extended[0]-1, pos_extended[1]+1)
        yield pos_extended
    while pos_extended != (x, y+r):
        pos_extended = (pos_extended[0] + 1, pos_extended[1]+1)
        yield pos_extended


main()
quit()
