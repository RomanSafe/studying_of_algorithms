import sys
from random import randint
from collections import Counter, namedtuple

def naive_version(list_of_segments, list_of_points):
    counter_list = []
    for point in list_of_points:
        counter = 0
        for segment in list_of_segments:
            if segment[0] <= point and segment[1] >= point:
                counter += 1
        counter_list.append(counter)
    return counter_list


def segments_points_comparing(list_of_segments, list_of_points):
    # not works properly
    def collecting_of_segments(list_of_segments, point):
        counter = 0
        less_then = 0
        equal = 0
        greater_then = 0
        sorted_segments = []
        for segment in list_of_segments:
            if segment[0] <= point:
                sorted_segments.append(segment)
        for segment in sorted_segments:
            if segment[1] >= point:
                counter += 1
        return  counter

    result_list = []
    for point in list_of_points:
        result_list.append(collecting_of_segments(list_of_segments, point))
    return result_list


def general():
    list_of_segments = []
    list_of_points = []
    input_obj = (tuple(map(int, line.split())) for line in sys.stdin)
    segments, points = next(input_obj)
    for segment in range(segments):
        list_of_segments.append(next(input_obj))
    list_of_points.extend(next(input_obj))
    results = segments_points_comparing(list_of_segments, list_of_points)
    for result in results:
        print(result, end=' ')

def test():
    from random import randint, randrange
    from timing import timed

    for attempt in range(1):
        n = randint(1, 50000)
        m = randint(1, 50000)
        points_list = [randint(1, 10**8) for _ in range(m)]
        segments_list = []
        for _ in range(n):
            coordinate = randint(1, 10 ** 8)
            segments_list.append((randrange(1, coordinate), coordinate))

        t1 = timed(naive_version, segments_list, points_list)
        t2 = timed(naive_version2, segments_list, points_list)
        # assert t < 3
        print("naive", t1)
        print("naive2", t2)


if __name__ == '__main__':
    test()
    # general()
