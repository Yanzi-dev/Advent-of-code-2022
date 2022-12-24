from collections import deque


def main():
    data = list()
    handle = open("input.txt")
    for line in handle:
        data.append(line.strip())

    height = len(data)
    width = len(data[0])

    i = j = 0
    while data[i][j] == "#":
        j += 1

    forbiddens = {}
    for time in range((height - 2) * (width - 2) + 1):
        forbid = set()
        for xx in range(height):
            for jj in range(width):
                if data[xx][jj] == ">":
                    forbid.add((xx, 1 + ((jj - 1 + time) % (width - 2))))
                elif data[xx][jj] == "v":
                    forbid.add((1 + ((xx - 1 + time) % (height - 2)), jj))
                elif data[xx][jj] == "<":
                    forbid.add((xx, 1 + ((jj - 1 - time) % (width - 2))))
                elif data[xx][jj] == "^":
                    forbid.add((1 + ((xx - 1 - time) % (height - 2)), jj))
        forbiddens[time] = forbid

    seen = set()
    start = (i, j, 0, False, False)
    queue = deque([start])
    result = list()
    while queue:
        (i, j, time, end, start) = queue.popleft()
        if not (0 <= i < height and 0 <= j < width and data[i][j] != "#"):
            continue
        if i == height - 1 and end and start:
            result.append(time)
            break
        if i == height - 1:
            result.append(time)
        if i == height - 1:
            end = True
        if i == 0 and end:
            start = True
        if (i, j, time, start, end) in seen:
            continue
        seen.add((i, j, time, start, end))
        forbid = forbiddens[time + 1]

        if (i, j) not in forbid:
            queue.append((i, j, time + 1, end, start))
        if (i + 1, j) not in forbid:
            queue.append((i + 1, j, time + 1, end, start))
        if (i - 1, j) not in forbid:
            queue.append((i - 1, j, time + 1, end, start))
        if (i, j + 1) not in forbid:
            queue.append((i, j + 1, time + 1, end, start))
        if (i, j - 1) not in forbid:
            queue.append((i, j - 1, time + 1, end, start))

    print("star1", result[0])
    print("star2", result[-1])


main()
quit()
