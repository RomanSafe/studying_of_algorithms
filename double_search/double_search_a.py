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


def test():
    assert double_search([0, 1, 2, 50, 75, 99, 100], 100) == 6
    assert double_search([0, 1, 2, 50, 75, 99, 100], 101) == -1
    assert double_search([0, 1, 2, 50, 75, 99, 100, 1000], 1001) == -1
    assert double_search([0, 1, 2, 50, 75, 99, 100000], 1000000) == -1


    from random import randint
    from timing import timed

    for attempt in range(10):
        n = randint(1, 10**5)
        search_where = [randint(1, 10**9) for _ in range(n)]
        search_where.sort()
        search_where.insert(0, n)
        n2 = randint(1, 10 ** 5)
        search_what = [randint(1, 10**9) for _ in range(n2)]
        search_what.insert(0, n2)
        t = search_what.pop(0)
        assert len(search_where) == search_where[0] + 1
        assert len(search_what) == t
        search_where[0] = 0
        for key in search_what:
            print(double_search(search_where, key), end=" ")

        t = timed(double_search, search_where, key)
        assert t < 3


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
    test()
    # main()

