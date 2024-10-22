# problem: https://adventofcode.com/2020/day/15


def read_file() -> list[int]:
    with open(file_name, "r") as file:
        return [int(number) for number in file.readline().strip().split(",")]


def calculate_number(goal_number: int) -> int:
    last_appearance = dict()
    last_number = numbers[-1]
    last_index = len(numbers) - 1
    for i in range(len(numbers) - 1):
        last_appearance[numbers[i]] = i

    while True:
        if last_index == goal_number - 1:
            break
        if last_number not in last_appearance:
            last_appearance[last_number] = last_index
            last_number = 0
        else:
            storage = last_number
            last_number = last_index - last_appearance[last_number]
            last_appearance[storage] = last_index

        last_index += 1

    return last_number


def star1(goal_number: int) -> int:
    return calculate_number(goal_number)


def star2(goal_number: int) -> int:
    return calculate_number(goal_number)


if __name__ == "__main__":
    file_name = "input.txt"
    numbers = read_file()

    print(star1(2020))
    print(star2(30000000))
