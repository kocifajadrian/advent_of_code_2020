# problem: https://adventofcode.com/2020/day/7


def read_file() -> None:
    with open(file_name, "r") as file:
        for line in file:
            bag, contents = line.strip().split(" bags contain ")
            bags[bag] = dict()
            if contents.endswith("no other bags."):
                continue
            for content in contents.split(", "):
                content = content.split(" ")
                bags[bag][f"{content[1]} {content[2]}"] = int(content[0])


def star1() -> int:
    counter = 0
    for bag in bags:
        stack = [b for b in bags[bag]]
        while len(stack):
            current_bag = stack.pop()
            if current_bag == goal_bag:
                counter += 1
                break
            for b in bags[current_bag]:
                stack.append(b)

    return counter


def star2() -> int:
    def number_of_bags(bag: str, number: int) -> int:
        if not len(bags[bag]):
            return number
        return number + number * sum(number_of_bags(b, bags[bag][b]) for b in bags[bag])

    return sum(number_of_bags(b, bags[goal_bag][b]) for b in bags[goal_bag])


if __name__ == "__main__":
    file_name = "input.txt"
    bags = dict()
    read_file()
    goal_bag = "shiny gold"

    print(star1())
    print(star2())
