import collections
import functools
import itertools
import re

valves, pressures, distances = set(), dict(), collections.defaultdict(lambda: 1000)

for valve, flow, leads, in re.findall(r"Valve (\w+) .*=(\d*); .* valves? (.*)", open("input.txt").read()):
    valves.add(valve)
    if flow != '0':
        pressures[valve] = int(flow)
    for lead in leads.split(', '):
        distances[lead, valve] = 1

# produit en croix
for k, i, j in itertools.product(valves, valves, valves):
    distances[i, j] = min(distances[i, j], distances[i, k] + distances[k, j])


@functools.cache
def search_1(time, cur="AA", valves=frozenset(pressures)):
    res = [0]
    for valve in valves:
        if distances[cur, valve] < time:
            res.append(pressures[valve] * (time - distances[cur, valve] - 1) + search_1(time - distances[cur, valve] - 1, valve, valves - {valve}))
    return max(res)


@functools.cache
def search_2(time, cur="AA", valves=frozenset(pressures), elephant=False):
    res = list()
    for valve in valves:
        if distances[cur, valve] < time:
            res.append(pressures[valve] * (time - distances[cur, valve] - 1) + search_2(time - distances[cur, valve] - 1, valve, valves - {valve}, elephant))
    return max(res + [search_2(26, valves=valves, elephant=False) if elephant else 0])


print("star1", str(search_1(30)))
print("star2", str(search_2(26, elephant=True)))
