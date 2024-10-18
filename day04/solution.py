# problem: https://adventofcode.com/2020/day/4


class Passport:
    def __init__(self) -> None:
        self.information = dict()


def read_file() -> None:
    with open(file_name, "r") as file:
        passports.append(Passport())
        for line in file:
            for element in line.strip().split(" "):
                if element == "":
                    passports.append(Passport())
                else:
                    x, y = element.split(":")
                    passports[-1].information[x] = y


def is_number(number: str) -> bool:
    try:
        int(number)
    except ValueError:
        return False
    return True


def byr_rule(value: str) -> bool:
    return is_number(value) and int(value) in byr_range


def iyr_rule(value: str) -> bool:
    return is_number(value) and int(value) in iyr_range


def eyr_rule(value: str) -> bool:
    return is_number(value) and int(value) in eyr_range


def hgt_rule(value: str) -> bool:
    if value.endswith("cm") and int(value[:-2]) in hgt_cm_range:
        return True
    if value.endswith("in") and int(value[:-2]) in hgt_in_range:
        return True
    return False


def hcl_rule(value: str) -> bool:
    return (value[0] == "#" and
            ["a" <= char <= "f" or "0" <= char <= "9" for char in value[1:]])


def ecl_rule(value: str) -> bool:
    return value in ecl_options


def pid_rule(value: str) -> bool:
    return is_number(value) and len(value) == pid_length


def star1() -> int:
    counter = len(passports)
    for passport in passports:
        for element in needed_information:
            if element not in passport.information:
                counter -= 1
                break

    return counter


def star2() -> int:
    counter = len(passports)
    for passport in passports:
        valid = True
        for element in needed_information:
            if element not in passport.information:
                counter -= 1
                break
            value = passport.information[element]
            match element:
                case "byr":
                    valid = byr_rule(value)
                case "iyr":
                    valid = iyr_rule(value)
                case "eyr":
                    valid = eyr_rule(value)
                case "hgt":
                    valid = hgt_rule(value)
                case "hcl":
                    valid = hcl_rule(value)
                case "ecl":
                    valid = ecl_rule(value)
                case "pid":
                    valid = pid_rule(value)
            if not valid:
                counter -= 1
                break

    return counter


if __name__ == "__main__":
    file_name = "input.txt"
    passports = []
    needed_information = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
    read_file()
    byr_range = range(1920, 2002 + 1)
    iyr_range = range(2010, 2020 + 1)
    eyr_range = range(2020, 2030 + 1)
    hgt_cm_range = range(150, 193 + 1)
    hgt_in_range = range(59, 76 + 1)
    ecl_options = {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}
    pid_length = 9

    print(star1())
    print(star2())
