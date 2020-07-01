def largest_not_incr_seq(n, array):
    # Failed test #12 of 20. Time limit exceeded
    from collections import deque

    count_array = [1] * n
    for i in range(n):
        for j in range(0, i):
            if array[i] <= array[j] and count_array[j] + 1 > count_array[i]:
                count_array[i] = count_array[j] + 1
    maxima = max(count_array)
    max_ind = count_array.index(maxima)
    deque = deque()
    deque.appendleft(max_ind + 1)
    temp_max = maxima
    for i in range(max_ind - 1, - 1, - 1):
        if count_array[i] == temp_max - 1:
            deque.appendleft(i + 1)
            temp_max -= 1
    result = list(deque)
    return (maxima, result)


def largest_not_incr_seq2(n, array):
    # it is not works
    def binary_search(where_to_find, num):
        left, right = 0, len(where_to_find)
        while left < right:
            middle = (right - left) // 2 + left
            if where_to_find[middle] >= num:
                left = middle + 1
            else:
                right = middle - 1
        return right

    from collections import deque
    last_num = [10**10]
    last_num += [-1] * n
    last_ind = [-1] * n
    prev_ind = [-1] * n
    length = 0
    for i in range(n + 1):
        j = binary_search(last_num, array[i])
        if last_num[j - 1] >= array[i] and last_num[j] < array[i]:
            last_num[j] = array[i]
            last_ind[j] = i
            prev_ind[i] = last_ind[j - 1]
            length = max(length, j)

    pointer = last_ind[length]
    answer = deque()
    while pointer != -1:
        answer.appendleft(last_ind[pointer])
        pointer = prev_ind[pointer]
    result = list(answer)
    return (length, result)

def largest_not_incr_seq3(n, array):
    from collections import deque
    deque = deque()
    sequences = [10**10] + [-1] * (n + 2)
    pre_result = [0] * (n + 1)
    last_ind = [0] * (n + 1)
    prev_ind = [0] * (n + 1)
    length = 1
    for i in range(n):
        left, right = 0, i + 2
        while left + 1 < right:
            middle = (right - left) // 2 + left
            if sequences[middle] >= array[i]:
                left = middle
            else:
                right = middle
        sequences[right] = array[i]
        pre_result[i] = right
        last_ind[i] = i + 1
        if right > length:
            length = right
    pointer = length
    for i in range(n, - 1, -1):
        if pre_result[i] == pointer:
            deque.appendleft(last_ind[i])
            pointer -= 1
    return (length, list(deque))

def general():
    import sys

    reader = sys.stdin
    n = int(reader.readline().rstrip())
    array = list(map(int, reader.readline().split()))
    k, ans_array = largest_not_incr_seq3(n, array)
    print(k)
    for a in ans_array:
        print(a, end=' ')


def test():
    assert largest_not_incr_seq(5, [5, 3, 4, 4, 2]) == largest_not_incr_seq3(5, [5, 3, 4, 4, 2])

    from random import randint
    from timing import timed

    for attempt in range(10):
        n = randint(1, 10 ** 5)
        search_where = [randint(0, 10 ** 9) for _ in range(n)]
        largest_not_incr_seq3(n, search_where)

        t = timed(largest_not_incr_seq3, n, search_where)
        assert t < 3


if __name__ == '__main__':
    general()
    # test()
