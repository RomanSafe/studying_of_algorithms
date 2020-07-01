from collections import deque

def wraper(array, array_len):
    def invertion_counter(array, l, m, r):
        counter = 0
        temp_store = deque()
        left_ind = l
        middle_plus = m + 1
        right_ind = r
        while left_ind <= m and middle_plus <= right_ind:
            if array[left_ind] > array[middle_plus]:
                temp_store.append(array[middle_plus])
                counter += m - left_ind + 1
                middle_plus += 1
            else:
                temp_store.append(array[left_ind])
                left_ind += 1
        while left_ind <= m:
            temp_store.append(array[left_ind])
            left_ind += 1
        while middle_plus <= right_ind:
            temp_store.append(array[middle_plus])
            middle_plus += 1
        left_ind = l
        right_ind = r
        while temp_store and left_ind <= right_ind:
            array[left_ind] = temp_store.popleft()
            left_ind += 1
        return counter


    def merge_sort(array, left_ind, right_ind):
        nonlocal counter
        if left_ind < right_ind:
            middle = int((left_ind + right_ind) / 2)
            merge_sort(array, left_ind, middle)
            merge_sort(array, middle + 1, right_ind)
            counter += invertion_counter(array, left_ind, middle, right_ind)
            return
        else:
            return

    counter = 0
    merge_sort(array, 0, array_len - 1)
    return counter


def general():
    array_len = int(input())
    array = list(map(int, input().split(" ")))
    if array_len <= 1:
        return 0
    assert len(array) == array_len
    return print(wraper(array, array_len))

def test():
    assert wraper([1, 100, 2, 50, 75, 99, 10], 7) == 8
    assert wraper([7, 6, 5, 4, 3, 2, 1], 7) == 21
    assert wraper([1, 3, 4, 5, 6, 2], 6) == 4
    assert wraper([2, 3, 9, 2, 9], 5) == 2
    assert wraper([0, 1, 2, 50, 75, 99, 100], 7) == 0
    assert wraper([1, 2, 3, 5, 4], 5) == 1

    # from random import randint
    # from timing import timed
    #
    # for attempt in range(2):
    #     n = randint(1, 10**5)
    #     sample_list = [randint(1, 10**9) for _ in range(n)]
    #     assert len(sample_list) == n
    #     # assert wraper(sample_list, n) >= 1
    #     sample_list.sort()
    #     assert wraper(sample_list, n) == 0
    #
    #
    #     t = timed(wraper, sample_list, n)
    #     assert t < 3


if __name__ == '__main__':
    # general()
    test()
