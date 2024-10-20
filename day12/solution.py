# problem: https://adventofcode.com/2020/day/12


def read_file() -> None:
    with open(file_name, "r") as file:
        for line in file:
            name = line[0]
            value = int(line[1:].strip())
            instructions.append((name, value))


def manhattan_distance(position: list[int]) -> int:
    return abs(position[0] - position[2]) + abs(position[1] - position[3])


def star1() -> int:
    position = [0, 0, 0, 0]
    direction = 1
    for instruction in instructions:
        name, value = instruction
        if name in directions:
            position[directions[name]] += value
        elif name == "F":
            position[direction] += value
        elif name == "R":
            direction = (direction + value // 90) % len(position)
        else:
            direction = (direction - value // 90) % len(position)

    return manhattan_distance(position)


def star2() -> int:
    position = [0, 0, 0, 0]
    way_point = [1, 10, 0, 0]
    for instruction in instructions:
        name, value = instruction
        if name in directions:
            way_point[directions[name]] += value
        elif name == "F":
            for i in range(len(position)):
                position[i] += way_point[i] * value
        else:
            for _ in range((value % 360) // 90):
                if name == "R":
                    way_point.insert(0, way_point.pop(-1))
                if name == "L":
                    way_point.append(way_point.pop(0))

    return manhattan_distance(position)


if __name__ == "__main__":
    file_name = "input.txt"
    instructions = []
    directions = {"N": 0, "E": 1, "S": 2, "W": 3}
    read_file()

    print(star1())
    print(star2())
