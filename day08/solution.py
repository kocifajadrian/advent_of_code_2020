# problem: https://adventofcode.com/2020/day/8


class Instruction:
    def __init__(self, name: str, value: int) -> None:
        self.name = name
        self.value = value


def read_file() -> None:
    with open(file_name, "r") as file:
        for line in file:
            name, value = line.strip().split(" ")
            instructions.append(Instruction(name, int(value)))


def terminates(edited_instructions: list[Instruction]) -> tuple[bool, int]:
    accumulator = 0
    index = 0
    visited = set()

    while index not in visited:
        visited.add(index)
        current_instruction = instructions[index]
        match current_instruction.name:
            case "acc":
                accumulator += current_instruction.value
                index += 1
            case "jmp":
                index += current_instruction.value
            case "nop":
                index += 1
        if index == len(edited_instructions):
            return True, accumulator

    return False, accumulator


def star1() -> int:
    return terminates(instructions)[1]


def star2() -> int:
    for i in range(len(instructions)):
        name = instructions[i].name
        if name == "nop":
            instructions[i].name = "jmp"
        if name == "jmp":
            instructions[i].name = "nop"
        if name == "acc":
            continue
        ends, value = terminates(instructions)
        instructions[i].name = name
        if ends:
            return value

    return 0


if __name__ == "__main__":
    file_name = "input.txt"
    instructions = []
    read_file()

    print(star1())
    print(star2())
