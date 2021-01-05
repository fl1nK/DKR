F = input("Введіть булеву функцію ")
if (len(F) != 8):
    print("Неправильно введено функцію")
    exit()
for i in F:
    if (i != "0" and i != "1"):
        print("Неправильно введено функцію")
        exit()

n = 0
print("x", "y", "z ", "F")
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            print(x, y, z, "", F[n])
            n += 1


def const0():
    n = 0
    for x in 0, 1:
        for y in 0, 1:
            for z in 0, 1:
                if (x == 0 and y == 0 and z == 0 and F[n] == "0"):
                    return "Збергіє константу 0"
                n += 1
    return "Не збергіє константу 0"


def const1():
    n = 0
    for x in 0, 1:
        for y in 0, 1:
            for z in 0, 1:
                if (x == 1 and y == 1 and z == 1 and F[n] == "1"):
                    return "Збергіє константу 1"
                n += 1
    return "Не збергіє константу 1"


def selfdual():
    not_F = ""
    for i in range(len(F)):
        if (F[i] == "0"):
            not_F += "1"
        else:
            not_F += "0"
    not_F = not_F[::-1]
    if (F == not_F):
        return "Самодвоїста"
    else:
        return "Несамодвоїста"


def ddnf():
    n = 0
    result = ""
    result1 = ""
    for x in 0, 1:
        for y in 0, 1:
            for z in 0, 1:
                if (F[n] == "1"):
                    if (x == 1):
                        result += "(x"
                    else:
                        result += "(x'"
                    if (y == 1):
                        result += "y"
                    else:
                        result += "y'"
                    if (z == 1):
                        result += "z)"
                    else:
                        result += "z')"
                    result += "\/"
                n += 1
    for let in range(len(result) - 2 ):
        result1 += result[let]
    return "ДДНФ:" + result1


def dknf():
    n = 0
    result = ""
    for x in 0, 1:
        for y in 0, 1:
            for z in 0, 1:
                if (F[n] == "0"):
                    if (x == 1):
                        result += "(x'\/"
                    else:
                        result += "(x\/"
                    if (y == 1):
                        result += "y'\/"
                    else:
                        result += "y\/"
                    if (z == 1):
                        result += "z')"
                    else:
                        result += "z)"
                n += 1
    return "ДКНФ:" + result


def linear_help(a, n):
    for i in 0, 1:
        ax = i
        if (int(F[n]) == a ^ ax):
            return ax


def linear():
    global a0, a2, a3, a1, a12, a23, a13, a123
    for x in 0, 1:
        for y in 0, 1:
            for z in 0, 1:
                if x == 0 and y == 0 and z == 0:
                    a0 = int(F[0])
                if x == 0 and y == 0 and z == 1:
                    a3 = linear_help(a0, 1)
                if x == 0 and y == 1 and z == 0:
                    a2 = linear_help(a0, 2)
                if x == 0 and y == 1 and z == 1:
                    a23 = linear_help(a0 ^ a3 ^ a2, 3)
                if x == 1 and y == 0 and z == 0:
                    a1 = linear_help(a0, 4)
                if x == 1 and y == 0 and z == 1:
                    a13 = linear_help(a0 ^ a1 ^ a3, 5)
                if x == 1 and y == 1 and z == 0:
                    a12 = linear_help(a0 ^ a1 ^ a2, 6)
                if x == 1 and y == 1 and z == 1:
                    a123 = linear_help(a0 ^ a1 ^ a2 ^ a3 ^ a12 ^ a13 ^ a23, 7)
    if a12 == 0 and a13 == 0 and a23 == 0 and a123 == 0:
        return "Функція лінійна"
    else:
        return "Функція нелінійна"




print("1." + const0())
print("2." + const1())
print("3." + selfdual())
print("4." + linear())
print("5." + ddnf())
print("6." + dknf())
