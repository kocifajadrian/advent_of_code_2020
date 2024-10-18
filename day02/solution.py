# problem: https://adventofcode.com/2020/day/2


class Password:
    def __init__(self, line: str) -> None:
        numbers, letter, password = line.split(" ")
        number1, number2 = [int(number) for number in numbers.split("-")]
        self.number1 = number1
        self.number2 = number2
        self.letter = letter[:-1]
        self.content = password


def read_file() -> None:
    with open(file_name, "r") as file:
        for line in file:
            passwords.append(Password(line))


def star1() -> int:
    counter = 0
    for password in passwords:
        value = password.content.count(password.letter)
        if value in range(password.number1, password.number2 + 1):
            counter += 1

    return counter


def star2() -> int:
    counter = 0
    for password in passwords:
        first = password.content[password.number1 - 1] == password.letter
        second = password.content[password.number2 - 1] == password.letter
        if (first or second) and not (first and second):
            counter += 1

    return counter


if __name__ == "__main__":
    file_name = "input.txt"
    passwords = []
    read_file()

    print(star1())
    print(star2())
