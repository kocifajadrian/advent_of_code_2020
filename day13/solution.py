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


def star2() -> int:
    return 0


if __name__ == "__main__":
    file_name = "input.txt"
    busses = []
    busses_index = dict()
    timestamp = read_file()

    print(star1())
    print(star2())
