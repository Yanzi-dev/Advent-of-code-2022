import queue


def main():
    print("Day 12 L-l-u-u-r-r-k-k-e-e-r-r-s-s")

    data = list()
    handle = open("input.txt")
    for line in handle:
        data.append(list(line.strip()))

    height = len(data)
    width = len(data[0])
    start = (0, 0)
    end = (0, 0)
    for i in range(height):
        for j in range(width):
            if data[i][j] == "S":
                start = (i, j)
                data[i][j] = "a"
            if data[i][j] == "E":
                end = (i, j)
                data[i][j] = "z"
    parcours_largeur_star1(start, end, data)
    print("star 2", parcours_largeur_star2(end, data))


def parcours_largeur_star1(start, end, data):
    q = queue.Queue()
    q.put(start)
    dist = {start: 0}

    closed_set = set()

    while q:
        current = q.get()

        if current == end:
            print("star 1", dist[current])
            break
        for n in get_eligible_coords_star1(current, data):
            if n in closed_set:
                continue
            dist[n] = dist[current]+1
            q.put(n)
            closed_set.add(n)


def parcours_largeur_star2(end, data):
    q = queue.Queue()
    q.put(end)
    dist = {end: 0}

    closed_set = set()

    while q:
        current = q.get()
        if data[current[0]][current[1]] == "a":
            return dist[current]
        for n in get_eligible_coords_star2(current, data):
            if n in closed_set:
                continue
            dist[n] = dist[current]+1
            q.put(n)
            closed_set.add(n)


def get_eligible_coords_star1(current_pos, data):
    i, j = current_pos
    coords = []
    for (x, y) in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        pos_x, pos_y = i + x, j + y
        if not 0 <= pos_x < len(data):
            continue
        if not 0 <= pos_y < len(data[0]):
            continue
        if ord(data[pos_x][pos_y]) > ord(data[i][j]) + 1:
            continue
        coords.append((pos_x, pos_y))
    return coords


def get_eligible_coords_star2(current_pos, data):
    i, j = current_pos
    coords = []
    for (x, y) in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        pos_x, pos_y = i + x, j + y
        if not 0 <= pos_x < len(data):
            continue
        if not 0 <= pos_y < len(data[0]):
            continue
        if ord(data[pos_x][pos_y]) < ord(data[i][j]) - 1:
            continue
        coords.append((pos_x, pos_y))
    return coords


main()
quit()
