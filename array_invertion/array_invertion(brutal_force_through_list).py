def array_invertion(array, number):
    counter = 0
    for i in range(0, number):
        for j in range(i + 1, number):
            if array[i] > array[j]:
                counter += 1
    return counter


def general():
    number = int(input())
    array = list(map(int, input().split(" ")))
    assert len(array) == number
    print(array_invertion(array), number)


def test():
    assert array_invertion([0, 1, 2, 50, 75, 99, 100], 7) == 0
    assert array_invertion([0, 100, 2, 50, 75, 99, 10], 7) == 8
    assert array_invertion([7, 6, 5, 4, 3, 2, 1], 7) == 21
    assert array_invertion([1, 2, 3, 5, 4], 5) == 1
    assert array_invertion([1, 3, 4, 5, 6, 2], 6) == 4


    from random import randint
    from timing import timed

    for attempt in range(10):
        n = randint(1, 10**5)
        search_where = [randint(1, 10**9) for _ in range(n)]
        search_where.sort()
        assert len(search_where) == n
        search_where.insert(0, 0)
        assert array_invertion(search_where, n) == 0

        t = timed(array_invertion, search_where, n)
        assert t < 3


if __name__ == '__main__':
    test()
