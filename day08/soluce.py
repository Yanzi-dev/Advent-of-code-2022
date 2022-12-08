import numpy


def main():
    with open("input.txt", "r") as file:
        lines = file.read().strip().split()

    matrix = [list(map(int, list(line))) for line in lines]
    height = len(matrix)
    width = len(matrix[0])
    visible_count = 0
    matrix = numpy.array(matrix)
    for i in range(height):
        for j in range(width):
            tree_size = matrix[i, j]
            if j == 0 or numpy.amax(matrix[i, :j]) < tree_size:
                visible_count += 1
            elif j == width - 1 or numpy.amax(matrix[i, (j+1):]) < tree_size:
                visible_count += 1
            elif i == 0 or numpy.amax(matrix[:i, j]) < tree_size:
                visible_count += 1
            elif i == height - 1 or numpy.amax(matrix[(i+1):, j]) < tree_size:
                visible_count += 1

    nsew = [[-1, 0], [1, 0], [0, 1], [0, -1]]
    scenic_scores_list = list()
    for i in range(height):
        for j in range(width):
            tree_size = matrix[i, j]
            scenic_score = 1
            # north south east west
            for direction_i, direction_j in nsew:
                x, y = i + direction_i, j + direction_j
                distance = 0

                while (0 <= x < height and 0 <= y < width) and matrix[x, y] < tree_size:
                    distance += 1
                    x += direction_i
                    y += direction_j
                    if (0 <= x < height and 0 <= y < width) and matrix[x, y] >= tree_size:
                        distance += 1
                scenic_score *= distance
            scenic_scores_list.append(scenic_score)

    print("star1: ", visible_count)
    print("star2: ", max(scenic_scores_list))


main()
quit()
