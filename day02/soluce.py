A = X = "Rock"
B = Y = "Paper"
C = Z = "Scissors"

Rock = 1
Paper = 2
Scissors = 3


def play_shifumi_score(j1: str, j2: str) -> int:
    score = 0
    if j1 == j2:
        score += eval(j2) + 3
    elif j1 == A:
        if j2 == Y:
            score += eval(j2) + 6
        elif j2 == Z:
            score += eval(j2)
    elif j1 == B:
        if j2 == X:
            score += eval(j2)
        elif j2 == Z:
            score += eval(j2) + 6
    elif j1 == C:
        if j2 == X:
            score += eval(j2) + 6
        elif j2 == Y:
            score += eval(j2)
    return score


def get_move_following_strategy(i1: str, strat: str) -> str:
    i2 = ""
    if strat == "X":
        if i1 == A:
            i2 = C
        if i1 == B:
            i2 = A
        if i1 == C:
            i2 = B
    elif strat == "Y":
        i2 = i1
    elif strat == "Z":
        if i1 == A:
            i2 = B
        if i1 == B:
            i2 = C
        if i1 == C:
            i2 = A
    return i2


def main():
    hand = open('input.txt')

    # star 1
    score = 0
    for line in hand:
        s = line.split()
        i1 = eval(s[0])
        i2 = eval(s[1])
        score += play_shifumi_score(i1, i2)

    print(score)

    # star 2
    hand.seek(0)
    score = 0
    for line in hand:
        s = line.split()
        i1 = eval(s[0])
        i2 = get_move_following_strategy(i1, s[1])
        score += play_shifumi_score(i1, i2)
    print(score)


main()
quit()
