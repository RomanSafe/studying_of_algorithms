import sys

def double_search(search_where, key):
    left_side = 1
    right_side = len(search_where) - 1
    while left_side <= right_side:
        middle = int(left_side + (right_side - left_side) / 2)
        if search_where[middle] == key:
            return middle
        elif search_where[middle] > key:
            right_side = middle - 1
        else:
            left_side = middle + 1
    return -1


def main():
    reader = (list(map(int, line.split())) for line in sys.stdin)
    search_where = next(reader)
    search_what = next(reader)
    t = search_what.pop(0)
    assert len(search_where) == search_where[0] + 1
    assert len(search_what) == t
    search_where[0] = 0
    for key in search_what:
        print(double_search(search_where, key), end=" ")


if __name__ == '__main__':
    main()
