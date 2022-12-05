import re
import copy


def main():
    handle = open('input.txt')

    # retrieve number of crates
    crates_number = 0
    for line in handle:
        if "1" in line:
            crates_number = line.split()[-1]
            break
    handle.seek(0)

    # reads crates and instruction
    crates_read = list()
    instructions = list()
    for line in handle:
        if "[" in line:
            crates = list(line[:-1])
            # removing space between crates [4] ___ [5] => [4]___[5]
            del crates[3::4]
            crates_splitted = ["".join(crates)[idx:idx + 3] for idx in range(0, len("".join(crates)), 3)]
            crates_cleaned = [i.strip()[1:-1] for i in crates_splitted]
            crates_read.append(crates_cleaned)
        elif "move" in line:
            instruction = re.findall(r'\d+', line)
            instructions.append(instruction)

    # Reshaping Crates list
    crate_list_star1 = list()
    i = 0
    while i < int(crates_number):
        temp = list()
        for crates in reversed(crates_read):
            if len(crates) > i:
                if crates[i].isalpha():
                    temp.append(crates[i])
        crate_list_star1.append(temp)
        i += 1

    crate_list_star2 = copy.deepcopy(crate_list_star1)

    # following instructions
    for instruction in instructions:
        quantite = int(instruction[0])
        index_source = int(instruction[1]) - 1
        index_dest = int(instruction[2]) - 1
        racs_to_move = crate_list_star1[index_source][-quantite:]
        racs_to_move2 = crate_list_star2[index_source][-quantite:]

        for rac in reversed(racs_to_move):
            crate_list_star1[index_source].pop()
            crate_list_star1[index_dest].append(rac)
            crate_list_star2[index_source].pop()
        crate_list_star2[index_dest] += racs_to_move2

    print("star1", "".join(i[-1] for i in crate_list_star1))
    print("star2", "".join(i[-1] for i in crate_list_star2))


main()
quit()
