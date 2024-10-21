# problem: https://adventofcode.com/2020/day/13


def read_file() -> int:
    with open(file_name, "r") as file:
        time = int(file.readline().strip())
        index = 0
        for buss_id in file.readline().strip().split(","):
            if buss_id != "x":
                busses.append(int(buss_id))
                busses_index[int(buss_id)] = index
            index += 1

        return time


def closest_arrival(buss_id: int) -> int:
    if timestamp // buss_id == timestamp / buss_id:
        print((timestamp // buss_id) * (buss_id + 1))

    return timestamp // buss_id * buss_id + buss_id


def star1() -> int:
    closest_time = 10 ** 100
    closest_id = 10 ** 100
    for buss_id in busses:
        arrival = closest_arrival(buss_id)
        if arrival - timestamp < closest_time - timestamp:
            closest_time = arrival
            closest_id = buss_id

    return (closest_time - timestamp) * closest_id


def nsn(number1: int, number2: int) -> int:
    maximum = max(number1, number2)
    minimum = min(number1, number2)
    number = maximum
    while number % minimum != 0:
        number += maximum

    return number


def star2() -> int:
    result = busses[0]
    adding = busses[0]
    for i in range(1, len(busses)):
        buss_id = busses[i]
        difference = busses_index[buss_id]
        while (result + difference) % buss_id != 0:
            result += adding
        adding = nsn(adding, buss_id)

    return result


if __name__ == "__main__":
    file_name = "input.txt"
    busses = []
    busses_index = dict()
    timestamp = read_file()

    print(star1())
    print(star2())
