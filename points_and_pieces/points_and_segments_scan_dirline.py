import sys
from collections import namedtuple

def naive_version(list_of_segments, list_of_points):
    # long working time
    counter_list = []
    for point in list_of_points:
        counter = 0
        for segment in list_of_segments:
            if segment[0] <= point and segment[1] >= point:
                counter += 1
        counter_list.append(counter)
    return counter_list


def scan_dirline2(list_of_coordinates, dict_of_points):
    # wrong answer in test 4
    from operator import attrgetter

    dict_of_points = dict_of_points
    counter = 0
    def multisort(what_to_sort, specs):
        for key, reverse in reversed(specs):
            what_to_sort.sort(key=attrgetter(key), reverse=reverse)
        return what_to_sort

    multisort(list_of_coordinates, (('coordinate', False), ('type', True)))
    print(list_of_coordinates)
    for line in list_of_coordinates:
        counter += line.type
        if line.type == 0:
            dict_of_points[line.coordinate] = counter
    return dict_of_points


def scan_dirline(list_of_coordinates, dict_of_points):
    def partition(list_of_coord, left_ind, right_ind):
        list_of_coordinates = list_of_coord
        benchmark = list_of_coordinates[left_ind]
        benchmark_ind = left_ind
        for ind in range(benchmark_ind + 1, right_ind + 1):
            if list_of_coordinates[ind].coordinate <= benchmark.coordinate:
                benchmark_ind += 1
                temp = list_of_coordinates[ind]
                list_of_coordinates[ind] = list_of_coordinates[benchmark_ind]
                list_of_coordinates[benchmark_ind] = temp

        temp2 = list_of_coordinates[left_ind]
        list_of_coordinates[left_ind] = list_of_coordinates[benchmark_ind]
        list_of_coordinates[benchmark_ind] = temp2
        return benchmark_ind

    dict_of_points = dict_of_points
    counter = 0
    left_ind = 0
    right_ind = len(list_of_coordinates) - 1
    def quick_sort(list_of_coordinates, left_ind, right_ind):
        if left_ind >= right_ind:
            return
        middle = partition(list_of_coordinates, left_ind, right_ind)
        quick_sort(list_of_coordinates, left_ind, middle - 1)
        quick_sort(list_of_coordinates, middle + 1, right_ind)

    quick_sort(list_of_coordinates, left_ind, right_ind)
    print(list_of_coordinates)
    for line in list_of_coordinates:
        counter += line.type
        if line.type == 0:
            dict_of_points[line.coordinate] = counter
    print(dict_of_points)
    return dict_of_points


def scan_of_ends(list_of_coordinates, dict_of_p):
    list_of_begs = list_of_coordinates
    list_of_ends = list_of_coordinates
    def partition(list_of_coord, left_ind, right_ind):
        list_of_coordinates = list_of_coord
        benchmark = list_of_coordinates[left_ind]
        benchmark_ind = left_ind
        for ind in range(benchmark_ind + 1, right_ind + 1):
            if list_of_coordinates[ind].coordinate <= benchmark.coordinate:
                benchmark_ind += 1
                temp = list_of_coordinates[ind]
                list_of_coordinates[ind] = list_of_coordinates[benchmark_ind]
                list_of_coordinates[benchmark_ind] = temp

        temp2 = list_of_coordinates[left_ind]
        list_of_coordinates[left_ind] = list_of_coordinates[benchmark_ind]
        list_of_coordinates[benchmark_ind] = temp2
        return benchmark_ind

    dict_of_points = dict_of_p
    counter = 0
    left_ind = 0
    right_ind = len(list_of_coordinates) - 1
    def quick_sort(list_of_coordinates, left_ind, right_ind):
        if left_ind >= right_ind:
            return
        middle = partition(list_of_coordinates, left_ind, right_ind)
        quick_sort(list_of_coordinates, left_ind, middle - 1)
        quick_sort(list_of_coordinates, middle + 1, right_ind)

    quick_sort(list_of_coordinates, left_ind, right_ind)
    print(list_of_coordinates)
    for line in list_of_coordinates:
        counter += line.type
        if line.type == 0:
            dict_of_points[line.coordinate] = counter
    print(dict_of_points)
    return dict_of_points

def general():
    point = namedtuple("point", "coordinate, type")
    list_of_coordinates = []
    input_obj = (tuple(map(int, line.split())) for line in sys.stdin)
    segments, points = next(input_obj)
    for _segment in range(segments):
        begining, end = next(input_obj)
        list_of_coordinates.extend((point(begining, 1), point(end, -1)))
    tuple_of_points = next(input_obj)
    dict_of_points = {}
    for coordinate in tuple_of_points:
        list_of_coordinates.append(point(coordinate, 0))
        dict_of_points[coordinate] = 0
    result = scan_dirline2(list_of_coordinates, dict_of_points)
    for val in result.values():
        print(val, end=' ')


def test():
    from random import randint, randrange
    from timing import timed

    for attempt in range(3):
        point = namedtuple("point", "coordinate, type")
        list_of_coordinates = []
        n = randint(1, 50000)
        m = randint(1, 50000)

        for _ in range(n):
            coordinate = randint(1, 10 ** 8)
            list_of_coordinates.extend((point(randrange(1, coordinate), 1), point(coordinate, -1)))

        dict_of_points = {}
        for _ in range(m):
            coordinate = randint(1, 10 ** 8)
            list_of_coordinates.append(point(coordinate, 0))
            dict_of_points[coordinate] = 0

        t1 = timed(scan_dirline2, list_of_coordinates, dict_of_points)
        # assert t < 3
        print(t1)


if __name__ == '__main__':
    # test()
    general()
