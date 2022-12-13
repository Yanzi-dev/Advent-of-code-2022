from functools import cmp_to_key


def main():
    pair = 1
    result = 0
    handle = open("input.txt")
    for line in handle:
        packet1 = eval(line.strip())
        packet2 = eval(handle.readline().strip())
        handle.readline()
        if compare(packet1, packet2) == -1:
            result += pair
        pair += 1
    print("star 1", result)
    handle.seek(0)

    packets = list()
    for line in handle:
        if line.strip():
            packets.append(eval(line.strip()))
    # adding [[2]] and [[6]]
    packets.append([[2]])
    packets.append([[6]])
    packets.sort(key=cmp_to_key(compare))
    x = packets.index([[2]]) + 1
    y = packets.index([[6]]) + 1
    print("star 2", x*y)


def compare(p1, p2):
    if type(p1) is int and type(p2) is int:
        if p1 < p2:
            return -1
        elif p1 > p2:
            return 1
        else:
            return 0
    if type(p1) is list and type(p2) is list:
        for i in range(min(len(p1), len(p2))):
            comparison = compare(p1[i], p2[i])
            if comparison == -1:
                return -1
            elif comparison == 1:
                return 1
        else:
            return compare(len(p1), len(p2))
    p1_alt = [p1] if type(p1) is int else p1
    p2alt = [p2] if type(p2) is int else p2
    return compare(p1_alt, p2alt)


main()
quit()
