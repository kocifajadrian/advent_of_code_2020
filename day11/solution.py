# problem: https://adventofcode.com/2020/day/11


def read_file() -> tuple[int, int]:
    with open(file_name, "r") as file:
        text = [line.strip() for line in file]
        rows = len(text)
        columns = len(text[0])
        for yy in range(rows):
            for xx in range(columns):
                if text[yy][xx] == "L":
                    seats[(yy, xx)] = 0
    return rows, columns


def out_of_bounds(position: tuple[int, int]) -> bool:
    return not (0 <= position[0] < r and 0 <= position[1] < c)


def build_adjacent() -> None:
    for seat in seats:
        adjacent[seat] = set()
        yy, xx = seat
        for j in range(3):
            for i in range(3):
                possible_adjacent = (yy - 1 + j, xx - 1 + i)
                if possible_adjacent != seat and possible_adjacent in seats:
                    adjacent[seat].add(possible_adjacent)


def build_adjacent_see() -> None:
    for seat in seats:
        adjacent_see[seat] = set()
        yy, xx = seat
        for direction in directions:
            for i in range(1, max(r, c)):
                possible_adjacent = (yy + direction[0] * i, xx + direction[1] * i)
                if out_of_bounds(possible_adjacent):
                    break
                if possible_adjacent in seats:
                    adjacent_see[seat].add(possible_adjacent)
                    break


def adjacent_occupied(seat: tuple[int, int], adjacent_type: dict[tuple[int, int]: set[tuple[int, int]]]) -> int:
    return sum([seats[s] for s in adjacent_type[seat]])


def resolve(adjacent_type: dict[tuple[int, int]: set[tuple[int, int]]], rule: int) -> int:
    while True:
        changes = set()
        for seat in seats:
            value = adjacent_occupied(seat, adjacent_type)
            if (not seats[seat] and not value) or (seats[seat] and value >= rule):
                changes.add(seat)
        if not len(changes):
            break
        for seat in changes:
            seats[seat] = (seats[seat] + 1) % 2

    return sum([seats[seat] for seat in seats])


def reset_seats() -> None:
    for seat in seats:
        seats[seat] = 0


def star1() -> int:
    return resolve(adjacent, adjacent_rule)


def star2() -> int:
    return resolve(adjacent_see, adjacent_see_rule)


if __name__ == "__main__":
    file_name = "input.txt"
    seats = dict()
    adjacent = dict()
    adjacent_see = dict()
    adjacent_rule = 4
    adjacent_see_rule = 5
    directions = [(0, -1), (-1, 0), (0, 1), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    r, c = read_file()
    read_file()
    build_adjacent()
    build_adjacent_see()

    print(star1())
    reset_seats()
    print(star2())
