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


def set_bit_to_zero(number: int, bit_index: int) -> int:
    return number & ~(1 << bit_index)


def set_bit_to_one(number: int, bit_index: int) -> int:
    return number | (1 << bit_index)


def calculate_value(mask: str, value: int) -> int:
    for i in range(len(mask)):
        bit = mask[len(mask) - i - 1]
        if bit == "0":
            value = set_bit_to_zero(value, i)
        elif bit == "1":
            value = set_bit_to_one(value, i)

    return value


def calculate_addresses(mask: str, address: int) -> set[int]:
    addresses = set()
    indexes = []
    for i in range(len(mask)):
        bit = mask[len(mask) - i - 1]
        if bit == "1":
            address = set_bit_to_one(address, i)
        elif bit == "X":
            indexes.append(i)

    for i in range(2 ** len(indexes)):
        storage = address
        for j in range(len(indexes)):
            bit = 1 & (i >> j)
            bit_index = indexes[j]
            if bit == 1:
                storage = set_bit_to_one(storage, bit_index)
            else:
                storage = set_bit_to_zero(storage, bit_index)
            storage = storage | (bit << bit_index)
        addresses.add(storage)

    return addresses


def star1() -> int:
    for i in range(len(masks)):
        mask = masks[i]
        for mi in memory_instructions[i]:
            address, value = mi
            memory[address] = calculate_value(mask, value)

    return sum(memory.values())


def star2() -> int:
    for i in range(len(masks)):
        mask = masks[i]
        for mi in memory_instructions[i]:
            address, value = mi
            addresses = calculate_addresses(mask, address)
            for add in addresses:
                memory[add] = value

    return sum(memory.values())


if __name__ == "__main__":
    file_name = "input.txt"
    masks = []
    memory = dict()
    memory_instructions = []
    read_file()

    print(star1())
    memory.clear()
    print(star2())
