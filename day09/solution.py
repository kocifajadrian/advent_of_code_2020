# problem: https://adventofcode.com/2020/day/9


def read_file() -> None:
    with open(file_name, "r") as file:
        for line in file:
            numbers.append(int(line.strip()))


def star1() -> int:
    for index in range(preamble_size, len(numbers)):
        i = index - preamble_size
        j = index - 1
        preamble = numbers[i:j + 1]
        next_number = numbers[index]
        valid = False
        for number in preamble:
            if next_number - number in preamble and next_number - number != number:
                valid = True
                break
        if not valid:
            return next_number

    return 0


def star2() -> int:
    invalid_number = star1()
    i = 0
    j = 1
    while True:
        sub_numbers = [numbers[index] for index in range(i, j)]
        summation = sum(sub_numbers)
        if summation < invalid_number:
            j += 1
        elif summation > invalid_number:
            i += 1
        else:
            return min(sub_numbers) + max(sub_numbers)


if __name__ == "__main__":
    file_name = "input.txt"
    numbers = []
    preamble_size = 25
    read_file()

    print(star1())
    print(star2())
