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
    print(wraper(array, array_len))


if __name__ == '__main__':
    general()
