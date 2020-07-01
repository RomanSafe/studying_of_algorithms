def end_scan(b, en, points):
    # it works properly
    from bisect import bisect_left, bisect_right
    beginings = b
    beginings.sort()
    ends = en
    ends.sort()
    for point in points:
        a = bisect_right(beginings, point)
        b = bisect_left(ends, point)
        print(a - b, end=' ')


def general():
    import sys

    beginings = []
    ends = []
    list_of_points = []
    input_obj = (tuple(map(int, line.split())) for line in sys.stdin)
    segments, points = next(input_obj)
    for segment in range(segments):
        begining, end = next(input_obj)
        beginings.append(begining)
        ends.append(end)
    list_of_points.extend(next(input_obj))
    end_scan(beginings, ends, list_of_points)


if __name__ == '__main__':
    general()
