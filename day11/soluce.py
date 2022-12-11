def main():
    print("See you space Lurkers")
    data = open("input.txt").read().strip()

    monkeys = list()
    for monkey in data.split("\n\n"):
        members = monkey.split("\n")
        items = [int(x) for x in members[1].split(":")[1].replace(" ", "").split(",")]
        operation = members[2].split(":")[1]
        divisible = int(members[3].split()[-1])
        true = int(members[4].split()[-1])
        false = int(members[5].split()[-1])
        monkeys.append((items, operation, divisible, true, false, [0]))

    mod = 1
    for monkey in monkeys:
        mod *= monkey[2]

    tour = 0
    while tour < 10000:  # replace 10000 by 20 for star 1
        for i in range(len(monkeys)):
            items, operation, divisible, true, false, items_inspect_count = monkeys[i]
            for _ in range(len(items)):
                monkeys[i][5][0] = items_inspect_count[0]+1
                item = items[0]
                item %= mod  # this is for star 2
                operation_members = operation.split()
                if operation_members[-1].isnumeric():
                    operande = int(operation_members[-1])
                else:
                    operande = item

                if operation_members[-2] == "*":
                    items[0] = items[0] * operande
                elif operation_members[-2] == "+":
                    items[0] = items[0] + operande
                # items[0] = items[0] // 3  # this is for star 1

                if items[0] % divisible == 0:
                    monkeys[true][0].append(monkeys[i][0].pop(0))
                else:
                    monkeys[false][0].append(monkeys[i][0].pop(0))

        tour += 1

    monkeys_inspect_count = list()
    for monkey in monkeys:
        monkeys_inspect_count.append(sum(monkey[5]))
    monkeys_inspect_count.sort(reverse=True)
    print("star ", monkeys_inspect_count[0]*monkeys_inspect_count[1])


main()
quit()
