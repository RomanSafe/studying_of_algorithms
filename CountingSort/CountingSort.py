import sys

def CountingSort(array, n):
    max_num = max(array) + 1
    counter = [0] * max_num
    for i in array:
        counter[i] = counter[i] + 1
    for j in range(1, max_num):
        counter[j] = counter[j - 1] + counter[j]
    array2 = [0] * n
    for g in reversed(array):
        array2[counter[g] - 1] = g
        counter[g] -= 1
    return array2


if __name__ == '__main__':
    n = int(sys.stdin.readline())
    array = list(map(int, sys.stdin.readline().split()))
    result = CountingSort(array, n)
    for num in result:
        print(num, end=' ')
