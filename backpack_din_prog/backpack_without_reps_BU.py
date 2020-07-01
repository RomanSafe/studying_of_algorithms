import sys

def pack_backpack_without_reps_bu(max_weight, sizes_of_pieces, amount_of_pieces):
    possible_weight = tuple([i for i in range(amount_of_pieces + 1)] for _ in range(max_weight + 1))
    for weight in range(max_weight + 1):
        possible_weight[weight][0] = 0
    for item in range(amount_of_pieces + 1):
        possible_weight[0][item] = 0
    for item in range(1, amount_of_pieces + 1):
        for weight in range(1, max_weight + 1):
            possible_weight[weight][item] = possible_weight[weight][item - 1]
            if sizes_of_pieces[item - 1] <= weight:
                possible_weight[weight][item] = max(possible_weight[weight][item], possible_weight[weight - sizes_of_pieces[item - 1]][item - 1] + sizes_of_pieces[item - 1])
    return possible_weight[max_weight][amount_of_pieces]


def preparation():
    reading = (tuple(map(int, line.split())) for line in sys.stdin)
    max_weight, amount_of_pieces = next(reading)
    sizes = next(reading)
    print(pack_backpack_without_reps_bu(max_weight, sizes, amount_of_pieces))


if __name__ == '__main__':
    preparation()
