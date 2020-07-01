import sys

def find_pos(xs, query):
    lo, hi = 0, len(xs)
    while lo < hi:
        mid = (lo + hi) // 2
        if xs[mid] == query:
            return mid + 1
        elif xs[mid] < query:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1


def test():
    assert find_pos([], 42) == -1
    assert find_pos([42], 42) == 1
    assert find_pos([24], 42) == -1

def main():
    reader = (map(int, line.split()) for line in sys.stdin)
    n, *xs = next(reader)
    k, *queries = next(reader)
    for query in queries:
        print(find_pos(xs, query), end=" ")


if __name__ == '__main__':
    test()
    main()
