# problem: https://adventofcode.com/2020/day/3


def read_file() -> None:
    with open(file_name, "r") as file:
        for line in file:
            trees.append(line.strip())


def star1(slope: tuple[int, int]) -> int:
    counter = 0
    position = (0, 0)
    while position[1] < max_rows:
        if trees[position[1]][position[0]] == "#":
            counter += 1
        position = ((position[0] + slope[0]) % max_columns, position[1] + slope[1])

    return counter


def star2(slopes: list[tuple[int, int]]) -> int:
    result = 1
    for slope in slopes:
        result *= star1(slope)

    return result


if __name__ == "__main__":
    file_name = "input.txt"
    trees = []
    read_file()
    max_rows = len(trees)
    max_columns = len(trees[0])
    star1_slope = (3, 1)
    star2_slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

    print(star1(star1_slope))
    print(star2(star2_slopes))
