def star1():
    hand = open('input.txt')

    priority_list = list()
    for line in hand:
        sac = line.strip()
        compartiment1 = sac[0:len(sac)//2]
        compartiment2 = sac[len(sac)//2:]
        common_letters_set = set(compartiment1).intersection(set(compartiment2))
        for letter in common_letters_set:
            priority_list.append(ord(letter) - 96 if letter.islower() else ord(letter) - 38)
    print(sum(priority_list))


def star2():
    hand = open('input.txt')
    sac_list = list()
    for line in hand:
        sac_list.append(line.strip())
    sac_list_grouped = []
    list_temp = []
    for index, value in enumerate(sac_list, 1):
        list_temp.append(value)
        if index % 3 == 0 or index == len(sac_list):
            sac_list_grouped.append(list_temp)
            list_temp = []

    priority_list = list()
    for group in sac_list_grouped:
        common_letters_set = set(group[0]).intersection(group[1]).intersection(group[2])
        for letter in common_letters_set:
            priority_list.append(ord(letter) - 96 if letter.islower() else ord(letter)-38)
    print(sum(priority_list))


star1()
star2()
quit()
