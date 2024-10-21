# problem: https://adventofcode.com/2020/day/14


def read_file() -> None:
    with open(file_name, "r") as file:
        for line in file:
            information = line.strip().split(" = ")
            if information[0] == "mask":
                masks.append(information[1])
                memory_instructions.append([])
                continue
            address = int(information[0][4: -1])
            value = int(information[1])
            memory_instructions[-1].append((address, value))


def calculate_value(mask: str, value: int) -> int:
    for i in range(len(mask)):
        bit = mask[len(mask) - i - 1]
        if bit == "0":
            value = value & ~(1 << i)
        elif bit == "1":
            value = value | (1 << i)

    return value


def star1() -> int:
    for i in range(len(masks)):
        mask = masks[i]
        for mi in memory_instructions[i]:
            address, value = mi
            memory[address] = calculate_value(mask, value)

    return sum(memory.values())


def star2() -> int:
    return 0


if __name__ == "__main__":
    file_name = "input.txt"
    masks = []
    memory = dict()
    memory_instructions = []
    read_file()

    print(star1())
    print(star2())
