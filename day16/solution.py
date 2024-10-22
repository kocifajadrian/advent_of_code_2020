# problem: https://adventofcode.com/2020/day/16


def read_file() -> None:
    with open(file_name, "r") as file:
        text = [line.strip() for line in file.readlines()]
        switch = 0
        for line in text:
            if line in ["", "your ticket:", "nearby tickets:"]:
                switch += 1
            elif switch == 0:
                name, ranges = line.split(": ")
                ranges = ranges.split(" or ")
                ranges = [range(int(r[:r.index("-")]), int(r[r.index("-") + 1:]) + 1) for r in ranges]
                fields.append(name)
                field[name] = ranges
            elif switch == 2:
                your_ticket.append([int(value) for value in line.split(",")])
            elif switch == 4:
                tickets.append([int(value) for value in line.split(",")])


def valid_tickets() -> list[list[int]]:
    valid_t = []
    for ticket in tickets:
        valid_ticket = True
        for value in ticket:
            in_range = False
            for f in fields:
                for r in field[f]:
                    if value in r:
                        in_range = True
                        break
            if not in_range:
                valid_ticket = False
                break
        if valid_ticket:
            valid_t.append(ticket)

    return valid_t


def star1() -> int:
    result = 0
    for ticket in tickets:
        for value in ticket:
            valid = False
            for f in fields:
                for r in field[f]:
                    if value in r:
                        valid = True
            if not valid:
                result += value

    return result


def star2() -> int:
    valid_t = valid_tickets()
    names = []
    for j in range(len(valid_t[0])):
        values = [valid_t[i][j] for i in range(len(valid_t))]
        n = set(fields)
        for f in fields:
            for value in values:
                in_range = False
                for r in field[f]:
                    if value in r:
                        in_range = True
                if not in_range:
                    n -= {f}
        names.append(n)

    positions = dict()
    determined = set()
    while len(determined) != len(names):
        for i in range(len(names)):
            n = names[i] - determined
            if len(n) == 1:
                element = list(n)[0]
                determined.add(element)
                positions[element] = i

    result = 1
    for f in positions:
        if "departure" in f:
            result *= your_ticket[0][positions[f]]

    return result


if __name__ == "__main__":
    file_name = "input.txt"
    your_ticket = []
    tickets = []
    fields = []
    field = dict()
    read_file()

    print(star1())
    print(star2())
