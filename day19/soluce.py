import re
from collections import deque, namedtuple

State = namedtuple('State', [
    'ore', 'clay', 'obsidian', 'geodes', 'ore_robots', 'clay_robots', 'obsidian_robots', 'geode_robots', 'time'
])


def bfs(cost_ore, cost_clay, cost_obsidian_ore, cost_obsidian_clay, cost_geode_ore, cost_geode_obsidian, time):
    largest = 0
    state = State(0, 0, 0, 0, 1, 0, 0, 0, time)
    queue = deque()
    queue.append(state)
    seen = set()
    while queue:
        state = queue.popleft()
        ore, clay, obsidian, geode, ore_robots, clay_robots, obsidian_robots, geode_robots, time = state

        largest = max(largest, geode)
        if time == 0:
            continue

        max_cost = max([cost_ore, cost_clay, cost_obsidian_ore, cost_geode_ore])
        if ore_robots >= max_cost:
            ore_robots = max_cost
        if clay_robots >= cost_obsidian_clay:
            clay_robots = cost_obsidian_clay
        if obsidian_robots >= cost_geode_obsidian:
            obsidian_robots = cost_geode_obsidian
        if ore >= time * max_cost - ore_robots * (time - 1):
            ore = time * max_cost - ore_robots * (time - 1)
        if clay >= time * cost_obsidian_clay - clay_robots * (time - 1):
            clay = time * cost_obsidian_clay - clay_robots * (time - 1)
        if obsidian >= time * cost_geode_obsidian - obsidian_robots * (time - 1):
            obsidian = time * cost_geode_obsidian - obsidian_robots * (time - 1)

        state = (ore, clay, obsidian, geode, ore_robots, clay_robots, obsidian_robots, geode_robots, time)

        if state in seen:
            continue
        seen.add(state)

        assert ore >= 0 and clay >= 0 and obsidian >= 0 and geode >= 0, state
        queue.append(
            (
                ore + ore_robots,
                clay + clay_robots,
                obsidian + obsidian_robots,
                geode + geode_robots,
                ore_robots,
                clay_robots,
                obsidian_robots,
                geode_robots,
                time - 1
            )
        )
        if ore >= cost_ore:
            queue.append(
                (
                    ore - cost_ore + ore_robots,  # remove cost for build ore robot
                    clay + clay_robots,
                    obsidian + obsidian_robots,
                    geode + geode_robots,
                    ore_robots + 1,  # add the robot
                    clay_robots,
                    obsidian_robots,
                    geode_robots,
                    time - 1
                )
            )
        if ore >= cost_clay:
            queue.append(
                (
                    ore - cost_clay + ore_robots,  # remove cost for build clay robot
                    clay + clay_robots,
                    obsidian + obsidian_robots,
                    geode + geode_robots,
                    ore_robots,
                    clay_robots + 1,  # add the clay robot
                    obsidian_robots,
                    geode_robots,
                    time - 1
                )
            )
        if ore >= cost_obsidian_ore and clay >= cost_obsidian_clay:
            queue.append(
                (
                    ore - cost_obsidian_ore + ore_robots,  # remove cost for build obsidian robot
                    clay - cost_obsidian_clay + clay_robots,  # remove clay for build obsidian robot
                    obsidian + obsidian_robots,
                    geode + geode_robots,
                    ore_robots,
                    clay_robots,
                    obsidian_robots + 1,  # add the robot
                    geode_robots,
                    time - 1
                )
            )
        if ore >= cost_geode_ore and obsidian >= cost_geode_obsidian:
            queue.append(
                (
                    ore - cost_geode_ore + ore_robots,  # remove cost for build geode robot
                    clay + clay_robots,
                    obsidian - cost_geode_obsidian + obsidian_robots,  # remove cost for build geode robot
                    geode + geode_robots,
                    ore_robots, clay_robots,
                    obsidian_robots,
                    geode_robots + 1,  # add the robot
                    time - 1
                )
            )
    return largest


def main():
    print("Day 19 of lurk")
    soluce_part1 = 0
    soluce_part2 = 1
    handle = open("input.txt", "r")

    for iteration, line in enumerate(handle):
        values = [int(x) for x in re.findall(r'\d+', line)]

        identifier = values[0]
        ore_cost = values[1]
        clay_cost = values[2]
        obsidian_cost_ore = values[3]
        obsidian_cost_clay = values[4]
        geode_cost_ore = values[5]
        geode_cost_clay = values[6]

        largest_geodes_1 = bfs(ore_cost, clay_cost, obsidian_cost_ore, obsidian_cost_clay, geode_cost_ore, geode_cost_clay, 24)
        soluce_part1 += identifier * largest_geodes_1
        if iteration < 3:
            largest_geodes_2 = bfs(ore_cost, clay_cost, obsidian_cost_ore, obsidian_cost_clay, geode_cost_ore, geode_cost_clay, 32)
            soluce_part2 *= largest_geodes_2
    print("part1", soluce_part1)
    print("part2", soluce_part2)


main()
quit()
