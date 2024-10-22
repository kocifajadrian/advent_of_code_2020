# problem: https://adventofcode.com/2020/day/17


def read_file() -> tuple[int, int, int]:
    with open(file_name, "r") as file:
        text = [line.strip() for line in file.readlines()]
        for i in range(len(text)):
            for j in range(len(text[0])):
                if text[i][j] == "#":
                    active.add((i, j, 0))

        return len(text), len(text[0]), 0


def get_neighbours_3d(cube: tuple[int, int, int]) -> set[tuple[int, int, int]]:
    neighbours = set()
    y, x, z = cube
    for yy in range(y - 1, y + 2):
        for xx in range(x - 1, x + 2):
            for zz in range(z - 1, z + 2):
                if (yy, xx, zz) == cube:
                    continue
                neighbours.add((yy, xx, zz))

    return neighbours


def get_neighbours_4d(cube: tuple[int, int, int, int]) -> set[tuple[int, int, int, int]]:
    neighbours = set()
    y, x, z, w = cube
    for yy in range(y - 1, y + 2):
        for xx in range(x - 1, x + 2):
            for zz in range(z - 1, z + 2):
                for ww in range(w - 1, w + 2):
                    if (yy, xx, zz, ww) == cube:
                        continue
                    neighbours.add((yy, xx, zz, ww))

    return neighbours


def number_of_active_neighbours_3d(cube: tuple[int, int, int],
                                   active_cubes: set[tuple[int, int, int]]) -> int:
    counter = 0
    neighbours = get_neighbours_3d(cube)
    for neighbour in neighbours:
        if neighbour in active_cubes:
            counter += 1

    return counter


def number_of_active_neighbours_4d(cube: tuple[int, int, int, int],
                                   active_cubes: set[tuple[int, int, int, int]]) -> int:
    counter = 0
    neighbours = get_neighbours_4d(cube)
    for neighbour in neighbours:
        if neighbour in active_cubes:
            counter += 1

    return counter


def star1() -> int:
    are_active = active.copy()

    for i in range(cycles):
        to_be_active = set()
        for yy in range(-i - 1, max_y + 2 + i):
            for xx in range(-i - 1, max_x + 2 + i):
                for zz in range(-i - 1, max_z + 2 + i):
                    current_cube = (yy, xx, zz)
                    active_neighbours = number_of_active_neighbours_3d(current_cube, are_active)
                    if current_cube in are_active:
                        if active_neighbours in [2, 3]:
                            to_be_active.add(current_cube)
                        continue
                    if active_neighbours == 3:
                        to_be_active.add(current_cube)
        are_active = to_be_active.copy()

    return len(are_active)


def star2() -> int:
    are_active = set([cube + (0,) for cube in active])

    for i in range(cycles):
        to_be_active = set()
        for yy in range(-i - 1, max_y + 2 + i):
            for xx in range(-i - 1, max_x + 2 + i):
                for zz in range(-i - 1, max_z + 2 + i):
                    for ww in range(-i - 1, max_w + 2 + i):
                        current_cube = (yy, xx, zz, ww)
                        active_neighbours = number_of_active_neighbours_4d(current_cube, are_active)
                        if current_cube in are_active:
                            if active_neighbours in [2, 3]:
                                to_be_active.add(current_cube)
                            continue
                        if active_neighbours == 3:
                            to_be_active.add(current_cube)
        are_active = to_be_active.copy()

    return len(are_active)


if __name__ == "__main__":
    file_name = "input.txt"
    active = set()
    max_y, max_x, max_z = read_file()
    max_w = 0
    cycles = 6

    print(star1())
    print(star2())
