def main():
    print("Day 10 lurkers")
    handle = open("input.txt")

    registry = list()
    screen_grid = [[' '] * 40 for _ in range(6)]
    cycle = 0
    registry.append((cycle, 1, 1))

    for line in handle:
        registry_start_value = registry[-1][2]
        striped = line.strip()
        x = cycle // 40
        y = cycle % 40
        if registry_start_value - 1 <= y <= registry_start_value + 1:
            screen_grid[x][y] = "#"
        cycle += 1
        registry.append((cycle, registry_start_value, registry_start_value))

        if striped != "noop":
            instruction = striped.split()
            x = cycle // 40
            y = cycle % 40
            if registry_start_value - 1 <= y <= registry_start_value + 1:
                screen_grid[x][y] = "#"
            cycle += 1
            registry.append((cycle, registry_start_value, registry_start_value + int(instruction[-1])))

    signal_strengths = list()
    for registry_cycle in registry[20::40]:
        signal_strengths.append(registry_cycle[0] * registry_cycle[1])
    print("star1:", sum(signal_strengths))
    print("star2:")
    for line in screen_grid:
        print("".join(line))


main()
quit()
