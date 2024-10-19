# problem: https://adventofcode.com/2020/day/10


def read_file() -> None:
    with open(file_name, "r") as file:
        maximum = 0
        for line in file:
            adapter = int(line.strip())
            if maximum < adapter:
                maximum = adapter
            adapters.append(adapter)
        adapters.append(maximum + 3)


def star1() -> int:
    differences = {1: 0, 2: 0, 3: 0}
    for i in range(len(adapters) - 1):
        differences[adapters[i + 1] - adapters[i]] += 1

    return differences[1] * differences[3]


def star2() -> int:
    ways = {0: 1}
    for i in range(1, len(adapters)):
        value = 0
        for j in range(3):
            if adapters[i] - j - 1 in ways:
                value += ways[adapters[i] - j - 1]
        ways[adapters[i]] = value
    return ways[adapters[-1]]


if __name__ == "__main__":
    file_name = "input.txt"
    adapters = [0]
    read_file()
    adapters.sort()

    print(star1())
    print(star2())
