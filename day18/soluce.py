from collections import deque


def main():
    print("Day 18 of Lurk")
    cubes = set()
    min_x, min_y, min_z = 100, 100, 100
    max_x, max_y, max_z = 0, 0, 0
    handle = open("input.txt", "r")
    for line in handle:
        x, y, z = list(map(int, line.strip().split(",")))
        min_x = min(min_x, x)
        min_y = min(min_y, y)
        min_z = min(min_z, z)
        max_x = max(max_x, x)
        max_y = max(max_y, y)
        max_z = max(max_z, z)
        coord_tuple = (x, y, z)
        cubes.add(coord_tuple)
    coords_adj = [(0, 0, 1), (0, 1, 0), (1, 0, 0), (0, 0, -1), (0, -1, 0), (-1, 0, 0)]
    not_connected_surface_area_count = 0
    for x, y, z in cubes:
        count = 0
        for delta_x, delta_y, delta_z in coords_adj:
            px, py, pz = x + delta_x, y + delta_y, z + delta_z
            if (px, py, pz) in cubes:
                count +=1
        not_connected_surface_area_count += 6 - count
    print("star1", str(not_connected_surface_area_count))

    lowest_cube = (min_x - 1, min_y - 1, min_z - 1)
    external_cubes = []
    external_cubes_set = set()
    external_cubes_set.add(lowest_cube)

    queue_cubes = deque()
    queue_cubes.append(lowest_cube)

    while queue_cubes:
        current_cube = queue_cubes.popleft()
        current_x, current_y, current_z = current_cube
        external_cubes.append(current_cube)

        for delta_x, delta_y, delta_z in coords_adj:
            px, py, pz = current_x + delta_x  , current_y + delta_y, current_z + delta_z
            if px <min_x - 1 or px > max_x + 1 or py < min_y -1 or py > max_y + 1 or pz < min_z -1 or pz > max_z + 1:
                continue
            current_coords = (px, py, pz)
            if current_coords in cubes or current_coords in external_cubes_set:
                continue
            queue_cubes.append(current_coords)
            external_cubes_set.add(current_coords)
    
    external_surface_area_count = 0
    for x, y, z in external_cubes:
        count = 0
        for delta_x, delta_y, delta_z in coords_adj:
            px, py, pz = x + delta_x, y + delta_y, z + delta_z
            if (px, py, pz) in cubes:
                count += 1
        external_surface_area_count += count    
    print("star2", external_surface_area_count)


main()
quit()