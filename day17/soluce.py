from collections import defaultdict

with open("input.txt", "r") as f:
    s = f.read().strip()

g = [list(x) for x in s.split("\n")]

rocks = [
    [
        [1,0,0,0],
        [1,0,0,0],
        [1,0,0,0],
        [1,0,0,0]
    ],
    [
        [0,1,0,0],
        [1,1,1,0],
        [0,1,0,0],
        [0,0,0,0]
    ],
    [
        [0,0,1,0],
        [0,0,1,0],
        [1,1,1,0],
        [0,0,0,0]
    ],
    [
        [1,1,1,1],
        [0,0,0,0],
        [0,0,0,0],
        [0,0,0,0]
    ],
    [
        [1,1,0,0],
        [1,1,0,0],
        [0,0,0,0],
        [0,0,0,0]
    ]
]

plow = [3, 1, 1, 0, 2]
grid = defaultdict(int)
maxy = -1
pid = 0
px, py =  0, 0

px = 2
py = maxy + 3 + 4 - plow[pid]

def movepiece(dx, dy):
    global px, py, grid, pid
    npx, npy = px + dx, py + dy
    for i in range(4):
        for j in range(4):
            if rocks[pid][i][j] == 0:
                continue
            rpx = npx + i
            rpy = npy - j
            if rpx not in range(7):
                return False
            if rpy < 0:
                return False
            if grid[rpx, rpy] != 0:
                return False
    px += dx
    py += dy
    return True

def movedown():
    global px, py, grid, pid
    if not movepiece(0,-1):
        for i in range(4):
            for j in range(4):
                if rocks[pid][i][j] == 0:
                    continue
                rpx = px + i
                rpy = py - j
                assert grid[rpx, rpy] == 0
                grid[rpx, rpy] = 1
        return False
    return True

def gen_top_view():
    global grid
    maxys = [-17 for _ in range(7)]
    for (x, y), v in grid.items():
        if v == 1:
            maxys[x] = max(maxys[x], y)
    v = max(maxys)
    return tuple(m - v for m in maxys)

seen = {}
nump = 0
additionnal = 0
while nump < 1000000000000:
    for vid,c in enumerate(s):
        if c == "<":
            movepiece(-1, 0)
        elif c == ">":
            movepiece(1, 0)
        if not movedown():
            maxy = 0
            for (_, y), v in grid.items():
                if v == 1:
                    maxy = max(maxy, y)
            pid = (pid + 1) % len(rocks)
            px = 2
            py = maxy + 3 + 4 - plow[pid]
            nump += 1
            if nump == 2022:
                count = 0
                for (_, y), v in grid.items():
                    if v == 1:
                        count = max(count, y)
                print("star1", count + 1)
            if nump >= 1000000000000:
                break
            topv = gen_top_view()
            if (topv, pid, vid) in seen and nump >= 2022:
                oldnump, oldmaxy=seen[topv, pid, vid]
                repeat = (1000000000000-nump) // (nump - oldnump)
                # jump in the futur
                nump += (nump - oldnump) * repeat
                # differential
                additionnal += repeat * (maxy - oldmaxy)
                seen = {}
            seen[topv, pid, vid] = (nump, maxy)
        # print("\n".join("".join("#" if grid[x,y] == 1 else "." for x in range(7)) for y in range (20,-1,-1)))
        # _ = input()

count = 0
for (_, y), v in grid.items():
    if v == 1:
        count = max(count, y)
print("star2", count + 1 + additionnal)