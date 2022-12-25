fuels = {'2': 2, '1': 1, '0': 0, '-': -1, '=': -2}
decimals = dict(map(reversed, fuels.items()))

def convert_to_decimal(snafu):
    decimal = sum([(5 ** i) * fuels[digit] for i, digit in enumerate(reversed(snafu))])
    return decimal

def to_snafu(decimal):
    value = []

    while decimal > 0:
        reste = decimal % 5
        if reste > 2:
            decimal += reste
            value.append(decimals[reste -5])
        else:
            value.append(str(reste))
        decimal //= 5
    return ''.join(reversed(value))


def main():
    print("Day 25 Last day of Lurk")
    handle = open("input.txt")
    result = 0
    for line in handle:
        result += convert_to_decimal(line.strip())
    print("star1", str(to_snafu(result)))
    print("star2", "⭐")


main()
quit()
