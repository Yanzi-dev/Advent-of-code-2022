import sympy


def main():
    print("Day 21 of lurk")
    monkeys = dict()
    items = [line.strip() for line in open("input.txt")]
    for item in items:
        monkey_name, expression = item.split(": ")
        if expression.isdigit():
            monkeys[monkey_name] = int(expression)
        else:
            gauche, operation, droite = expression.split()
            if gauche in monkeys and droite in monkeys:
                monkeys[monkey_name] = eval(f"{monkeys[gauche]} {operation} {monkeys[droite]}")
            else:
                items.append(item)
    print("star1", int(monkeys["root"]))

    operande = dict()
    operande["+"] = lambda a, b: a + b
    operande["-"] = lambda a, b: a - b
    operande["*"] = lambda a, b: a * b
    operande["/"] = lambda a, b: a / b
    
    sympy_monkeys = dict()
    sympy_monkeys["humn"] = sympy.Symbol("")

    for item in items:
        monkey_name, expression = item.split(": ")
        if monkey_name in sympy_monkeys: continue
        if expression.isdigit():
            sympy_monkeys[monkey_name] = sympy.Integer(expression)
        else:
            gauche, operation, droite = expression.split()
            if gauche in sympy_monkeys and droite in sympy_monkeys:
                if monkey_name == "root":
                    print("star2", sympy.solve(sympy_monkeys[gauche] - sympy_monkeys[droite])[0])
                    break
                sympy_monkeys[monkey_name] = operande[operation](sympy_monkeys[gauche], sympy_monkeys[droite])
            else:
                items.append(item)


main()
quit()
