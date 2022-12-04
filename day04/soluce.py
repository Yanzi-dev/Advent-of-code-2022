def is_range_containing_range(range1: list, range2:list):
    # warning limit case arent catched there (advent of code u know)
    # you can also use "set" and "subset" function but.. well.. whatever
    return int(range1[0]) <= int(range2[0]) and int(range1[-1]) >= int(range2[-1])
    

def star1():
    print("day 03 Lurkers first part")
    handle = open("input.txt")
    result = 0
    for line in handle:
        pairs = line.strip().split(',')
        range1 = pairs[0].split('-')
        range2 = pairs[1].split('-')
        if (is_range_containing_range(range1, range2) or is_range_containing_range(range2, range1)):
            result+=1
    print(result)


def star2():
    print("Day 03 Lurkers second part")
    handle = open("input.txt")
    result = 0
    for line in handle:
        pairs = line.strip().split(',')
        pair1 = pairs[0].split('-')
        pair2 = pairs[1].split('-')
        range1 = range(int(pair1[0]), int(pair1[-1])+1)
        range2 = range(int(pair2[0]), int(pair2[-1])+1)
        if len(set(range1).intersection(range2)) > 0:
            print(range1, range2)
            result+=1

    print(result)

star1()
star2()
quit()