# problem: https://adventofcode.com/2020/day/5


def read_file() -> None:
    with open(file_name, "r") as file:
        for line in file:
            seats.append(line.strip())


def decode_string(string: str, minimum: int, maximum: int) -> int:
    for character in string:
        if character in ["F", "L"]:
            maximum = (minimum + maximum) // 2
        else:
            minimum = (minimum + maximum) // 2 + 1

    return minimum


def seat_id(seat: str) -> int:
    return (decode_string(seat[:7], row_minimum, row_maximum) * 8 +
            decode_string(seat[7:], column_minimum, column_maximum))


def star1() -> int:
    maximum = -big_number
    for seat in seats:
        value = seat_id(seat)
        if value > maximum:
            maximum = value

    return maximum


def star2() -> int:
    seat_ids = set()
    for seat in seats:
        seat_ids.add(seat_id(seat))

    value = set(range(min(seat_ids), max(seat_ids) + 1)) - seat_ids
    return list(value)[0]


if __name__ == "__main__":
    file_name = "input.txt"
    row_minimum = column_minimum = 0
    row_maximum = 127
    column_maximum = 7
    big_number = 10 ** 10
    seats = []
    read_file()

    print(star1())
    print(star2())
