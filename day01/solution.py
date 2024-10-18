# problem: https://adventofcode.com/2020/day/1


def read_file() -> None:
    with open(file_name, "r") as file:
        for line in file:
            numbers.append(int(line.strip()))


def star1() -> int:
    i = 0
    j = len(numbers) - 1
    while i < j:
        first = numbers[i]
        second = numbers[j]
        value = first + second
        if value == desired_sum:
            return first * second
        elif value < desired_sum:
            i += 1
        else:
            j -= 1

    return 0


def star2() -> int:
    for third in numbers:
        i = 0
        j = len(numbers) - 1
        while i < j:
            first = numbers[i]
            second = numbers[j]
            value = first + second + third
            if value == desired_sum:
                return first * second * third
            elif value < desired_sum:
                i += 1
            else:
                j -= 1

    return 0


if __name__ == "__main__":
    file_name = "input.txt"
    numbers = []
    desired_sum = 2020
    read_file()
    numbers.sort()

    print(star1())
    print(star2())
