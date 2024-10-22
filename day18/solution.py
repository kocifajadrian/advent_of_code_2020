# problem: https://adventofcode.com/2020/day/18


class Equation:
    def __init__(self, string: str) -> None:
        self.values = []
        self.parse(string)

    def parse(self, string: str) -> None:
        counter = 0
        s = ""
        for i, character in enumerate(string):
            if character == "(":
                if counter:
                    s += character
                counter += 1
            elif character == ")":
                counter -= 1
                if counter == 0:
                    self.values.append(Equation(s))
                    s = ""
                else:
                    s += character
            elif counter:
                s += character
            elif character == " ":
                if s:
                    self.values.append(s)
                    s = ""
            else:
                s += character

        if s:
            self.values.append(s)

    def evaluate(self, addition_first: bool) -> int:
        for i in range(0, len(self.values), 2):
            if isinstance(self.values[i], str):
                self.values[i] = int(self.values[i])
                continue
            self.values[i] = self.values[i].evaluate(addition_first)

        if addition_first:
            for i in range(0, len(self.values) - 2, 2):
                if self.values[i + 1] == "+":
                    self.values[i + 2] = self.values[i] + self.values[i + 2]
                    self.values[i] = 1
                    self.values[i + 1] = "*"

        result = self.values[0]
        for i in range(1, len(self.values), 2):
            if self.values[i] == "+":
                result += self.values[i + 1]
                continue
            result *= self.values[i + 1]

        return result


def read_file() -> None:
    with open(file_name, "r") as file:
        for line in file:
            equations1.append(Equation(line.strip()))
            equations2.append(Equation(line.strip()))


def star1() -> int:
    result = 0
    for equation in equations1:
        result += equation.evaluate(False)

    return result


def star2() -> int:
    result = 0
    for equation in equations2:
        result += equation.evaluate(True)

    return result


if __name__ == "__main__":
    file_name = "input.txt"
    equations1 = []
    equations2 = []
    read_file()

    print(star1())
    print(star2())
