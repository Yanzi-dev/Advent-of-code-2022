class Node:
    def __init__(self, name, parent, is_dir, size=None):
        self.name = name
        self.parent = parent
        self.childrens = [] if is_dir else None
        self.size = size


def get_size(folder, total, all_sizes: list):
    size = 0
    for child in folder.childrens:
        if child.childrens is not None:
            s, total, all_sizes = get_size(child, total, all_sizes)
            size += s
        else:
            size += child.size
    if size <= 100000:
        total += size
    all_sizes.append(size)
    return size, total, all_sizes


def main():
    root = Node('/', None, True)
    pwd = root

    with open("input.txt", "r") as file:
        line = file.readline()
        while line:
            args = line.strip().split()
            if args[1] == "cd":
                if args[2] == "/":
                    pwd = root
                elif args[2] == "..":
                    pwd = pwd.parent
                else:
                    for child in pwd.childrens:
                        if child.name == args[2]:
                            pwd = child
                            break
                line = file.readline()
            elif args[1] == "ls":
                already_computed = pwd.childrens != []
                line = file.readline()
                args = line.strip().split()
                while args and args[0] != '$':
                    if not already_computed:
                        pwd.childrens.append(Node(args[1], pwd, args[0] == "dir", int(args[0]) if args[0] != "dir" else None))
                    line = file.readline()
                    args = line.strip().split()

    current_usage, total_at_most_100000, all_sizes = get_size(root, 0, [])
    total_disk = 70000000
    unused_space_goal = 30000000
    unused_space = total_disk - current_usage
    required_space = unused_space_goal - unused_space

    smallest_size_that_carry = current_usage
    for size in all_sizes:
        if smallest_size_that_carry > size >= required_space:
            smallest_size_that_carry = size

    print("star1:", total_at_most_100000)
    print("star2:", smallest_size_that_carry)


main()
quit()
