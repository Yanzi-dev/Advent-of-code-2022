def main():
    # init
    hand = open('input.txt')
    i = 0
    calories = dict()
    for line in hand:
        if line != '\n':
            calories.setdefault(i, []).append(line.strip())
        else:
            i += 1

    # transformation
    for i, a in calories.items():
        calories[i] = sum(map(int, a))

    # max calories
    print(max(calories.values()))

    # sum calories of 3 top calories
    calories_values = list(calories.values())
    calories_values.sort(reverse=True)
    print(sum(calories_values[0:3]))


main()
quit()
