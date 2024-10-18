# problem: https://adventofcode.com/2020/day/6


class Person:
    def __init__(self, questions: str) -> None:
        self.questions = set(q for q in questions)


class Group:
    def __init__(self) -> None:
        self.people = []

    def add(self, person: Person) -> None:
        self.people.append(person)


def read_file() -> None:
    with open(file_name, "r") as file:
        groups.append(Group())
        for line in file:
            line = line.strip()
            if line == "":
                groups.append(Group())
                continue
            groups[-1].add(Person(line))


def star1() -> int:
    counter = 0
    for group in groups:
        questions = set()
        for person in group.people:
            questions |= person.questions
        counter += len(questions)

    return counter


def star2() -> int:
    counter = 0
    for group in groups:
        questions = group.people[0].questions
        for person in group.people[1:]:
            questions &= person.questions
        counter += len(questions)

    return counter


if __name__ == "__main__":
    file_name = "input.txt"
    groups = []
    read_file()

    print(star1())
    print(star2())
