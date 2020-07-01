import sys


def divider_seq(n, array):
    count_array = [1] * n
    for i in range(n):
        for j in range(0, i):
            if array[i] % array[j] == 0 and count_array[j] + 1 > count_array[i]:
                count_array[i] = count_array[j] + 1
    counter_k = 0
    for i in range(n):
        counter_k = max(counter_k, count_array[i])
    return counter_k

def general():
    reader = sys.stdin
    n = int(reader.readline().rstrip())
    array = list(map(int, reader.readline().split()))
    print(divider_seq(n, array))


def test():
    assert divider_seq(8, [3, 6, 7, 9, 12, 24, 73, 48]) == 5


if __name__ == '__main__':
    general()
    # test()
