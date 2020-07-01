def SimpleCountingSort(A):
    scope = max(A) + 1
    C = [0] * scope
    for x in A:
        C[x] += 1
    A[:] = []
    for number in range(scope):
        A += [number] * C[number]
    return A


if __name__ == '__main__':
    print(SimpleCountingSort([6, 5, 4, 4, 7, 1, 4, 5]))
